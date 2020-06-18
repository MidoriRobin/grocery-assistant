"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import *
from app.models import *
from werkzeug.security import check_password_hash
import random
from app.RecomHandler import RecomHandler
from datetime import date

###
# Routing for application.
###


#api routes

@app.route('/')
def home():
    """Render website's home page."""
    products = Products.query.filter_by().all()
    return render_template('home.html',products=products)


@app.route('/about/')
def about():
    """Render the website's about page."""

    product = ShoppingCart.query.filter_by(acc_num=1323).order_by(ShoppingCart.cart_id.desc()).first()
    print(product)

    return render_template('about.html')


@app.route('/secure-page')
@login_required
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data

            if int(username) in range(1234,1333):
                print("this is a test user..")
                user = Usr.query.filter_by(acc_num=username).first()
                print(user)
                login_user(user)
                session['cartid'] = user.get_cartid()
            else:
                print("not a test user..")
                user = Usr.query.filter_by(acc_num=username).first()
                if user is not None and check_password_hash(user.password, password):
                    login_user(user)

            return redirect(url_for('secure_page'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('cartid', None)
    logout_user()
    flash('You were logged out', 'success')
    return redirect(url_for('home'))

#User sign up route
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = UsrForm()
    #Collect data from form and save in database
    if request.method == 'POST' and form.validate_on_submit():
        fname= form.firstname.data
        lname= form.lastname.data
        sex = form.sex.data
        email= form.email.data
        phone = form.phonenumber.data
        city = form.city.data
        street = form.street.data
        hh_size = form.hhsize.data
        no_adults = form.adlts.data
        no_kids = form.kids.data
        marital_s = form.maritalstat.data
        diet_pref = form.dietpref.data
        password = form.password.data


        user = Usr(fname,lname,sex,email,phone,city,street,hh_size,
        no_adults,no_kids,marital_s,diet_pref,password)
        db.session.add(user)
        db.session.commit()

        flash('success','')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)



@login_manager.user_loader
def load_user(id):
    return Usr.query.get(id)


@app.route('/products')
def products():
    thing = 10

    page = request.args.get('page', 1, type=int)
    prodos = Item.query.filter_by().paginate(page,10,False)

    rows = Item.query.limit(10).all()

    if prodos.has_next:
        next_url = url_for('products', page=prodos.next_num)
    else:
        next_url = None

    if prodos.has_prev:
        prev_url = url_for('products', page=prodos.prev_num)
    else:
        prev_url = None

    return render_template('products.html', prods=rows, prodos=prodos.items, next=next_url, prev = prev_url)


@app.route('/products/<itemid>', methods=['GET'])
def product(itemid):
    list = []
    revform = ReviewForm()
    listform = ItemListForm()
    # list = RecomHandler.cont_bsd_fltr(1)
    print(list)
    item = Item.query.filter_by(item_id=itemid).first()

    slists = ShoppingList.query.filter_by(acc_num=current_user.acc_num).all()
    listform.listname.choices = [(list.list_id, list.name) for list in slists]
    flash("Displaying product")

    return render_template('/test-templates/product.html', item=item, revform=revform, listform=listform)

#The route can be changed to "TryThese" instead of "Recommended items"
@app.route('/TryThese/<userid>', methods=['GET'])
@login_required
def recomm(userid):

    """Renders the recommendation page for a specific user based on the
        items they previously rated."""

    print("Recomm works")
    #products = Products.query.filter_by().all()

# Prepares recommendations, compiles products in an array
    recomD = RecomHandler.recomHelper()
    cUser = Usr.query.filter_by(acc_num=userid).first()

# If statement to check if the user is a new user and has any previous recommendation
    if is_new(userid, recomD["uid"]):
        print("New user!")
        uRecom = RecomHandler.diet_cnvrtr(cUser.diet_pref)
        recomProd = fetch_recomm(1,uRecom)
    else:
        print("Old user..")
        uRecom = RecomHandler.rec_by_usr(userid, recomD)
        recomProd = fetch_recomm(2,uRecom)

# Dummy recommendations
    buylst = dummy_list()

# Getting the list of recommended products, using the predictions(INCOMPLETE)
    #p_list = Products.query.filter_by()
# Function to randomize
    #rprop = buylst + rdmizePredictions(products)
# W/o Dummy products
    randPred = rdmize_predictions(recomProd)
    print(randPred)
    return render_template('recommendation.html', recom=randPred)

#Cart----------------------------------------------
@app.route('/users/<userid>/cart', methods=['GET'])
@login_required
def cart(userid):
    """View items in users cart"""

    #Fetching the users shopping cart ID
    cart = ShoppingCart.query.filter_by(acc_num=userid).first()

    itemList = cart.fetch_all_items()

    status = [{
        "message": "cart successfully fetched",
        "cart": itemList
    }]

    flash("cart successfully fetched")
    #return status
    return render_template('/test-templates/cart.html', list=itemList)

@app.route('/items/<itemid>/<qty>/cart/<cartid>', methods=['GET'])
@login_required
def add_item_cart(itemid,qty,cartid):
    """Route to add item to a cart"""

    item = Usi(cartid, itemid, qty, date.today())
    db.session.add(item)
    db.session.commit()

    status = {
        "message": "item successfully added to cart"
    }

    print(status)
    flash("item successfully added to cart")
    return redirect(url_for('products'))

@app.route('/users/<userid>/cart/<itemid>', methods=['GET'])
@login_required
def remove_from_cart(userid,itemid):

    item = Usi.query.filter_by(cart_id=session['cartid'],item_id=itemid).first()

    db.session.delete(item)
    db.session.commit()

    status = [{
        "message": "Item deleted successfully"
    }]

    flash("Item deleted successfully")
    # return status
    return redirect(url_for('cart', userid=current_user.acc_num))

#Lists----------------------------------------------
@app.route('/users/<userid>/lists', methods=['POST'])
@login_required
def make_list(userid):
    """Route to add a new list to a user account"""

    if request.method == 'POST':
        list = ShoppingList(userid, request.form['name'], date.today())

        db.session.add(list)
        db.session.commit()

    status = [{
        "messsage": "List successfully created"
    }]

    flash("List successfully created")
    # return status
    return redirect(url_for('view_lists'))

@app.route('/users/<userid>/lists', methods=['GET'])
@login_required
def view_lists(userid):
    """Route to view all lists of a specific user"""

    lists = ShoppingList.query.filter_by(acc_num=userid).all()

    status = [{
        "Message": "Displaying all shopping lists based on user id"
    }]

    flash("Displaying all shopping lists based on user id")
    #return status
    return render_template('/test-templates/lists.html', LoL=lists)

@app.route('/users/<userid>/lists/<listid>', methods=['GET'])
@login_required
def list(userid,listid):
    """Route to view a list of a specific user"""

    list = ShoppingList.query.filter_by(list_id=listid).first()
    items = list.view_items()
    status = [{
        "Message": "Displaying all items in the shopping list chosen"
    }]

    flash("Displaying all items in the shopping list chosen")
    #return status
    return render_template('/test-templates/list.html', items=items, list=list)

@app.route('/items/<itemid>/list/', methods=['POST'])
@login_required
def add_item_list(itemid):
    """Route to add an item to a specific list"""

    #sList = ShoppingList.query.filter_by(list_id=listid).first()

    if request.method == 'POST':
        # sList.add_item(itemid, date.today)

        if request.form['quantity'] != '':
            nItem = ListItem(request.form['listname'], itemid, date.today(), request.form['quantity'])
        else:
            nItem = ListItem(request.form['listname'], itemid, date.today(), 1)
        db.session.add(nItem)
        db.session.commit()

    status = [{
        "message": "Item added to list"
    }]

    flash("Item added to list")
    # return status
    return redirect(url_for('product',itemid=itemid))

@app.route('/users/list/<listid>/<itemid>', methods=['GET'])
@login_required
def remove_from_list(listid,itemid):

    item = ListItem.query.filter_by(list_id=listid, item_id=itemid).first()

    db.session.delete(item)
    db.session.commit()

    status = [{
        "message": "Item successfully deleted"
    }]

    flash("Item successfully deleted")
    # return status
    return redirect(url_for('list', listid=listid, userid=current_user.acc_num))

#Courier----------------------------------------------
@app.route('/courier', methods=['GET'])
def courier(arg):
    """Shows a list of couriers"""
    pass

# @app.route('')
# def chs_courier(arg):
#     pass

#Order----------------------------------------------
@app.route('/order/<userid>', methods=['GET'])
def view_order(arg):
    pass

@app.route('/user/<userid>/order', methods=['POST'])
def make_order(userid):
    #IMplement simulated order cart-table > order-table
    pass

#Review----------------------------------------------

@app.route('/items/<itemid>/review/', methods=['GET','POST'])

def review_item(itemid):

    if request.method == 'POST':
        rCheck = Review.query.filter_by(acc_num=request.form['userid'], item_id=request.form['itemid']).first()

        if rCheck:
            rCheck.rating = request.form['rating']
        else:
            review = Review(request.form['userid'],request.form['itemid'],request.form['rating'])
            db.session.add(review)

    db.session.commit()

    status = [{
        "message": "Review successfully added"
    }]

    flash("Review successfully added")
    # return status
    return redirect(url_for('products',itemid=itemid))


#Locally required functions

def rdmize_predictions(product_list):
    """
    Fetches, six random products from a list of predictions.
    """
    six_rand_prod = []
    r_num = len(product_list)

    print("Starting randomization..")
    while len(six_rand_prod) < 6:
        prod = product_list[random.randrange(0,r_num)]
        if prod in six_rand_prod:
            continue
        else:
            six_rand_prod.append(prod)

    print("Complete..")
    return six_rand_prod

def dummy_list():
    """Generates a list of dummy products, and returns them as a list of products.
    """

    pro1 = Products(101, "Chef's Select Tuna", "F001", "tuna.png", "High quality tuna for a high quality customer",
                    2000.00)

    pro2 = Products(102, "Pristine Banana Porridge", "F002", "porridge.png",
                        "porridge of the gods", 250.00)

    pro3 = Products(103, "Empire Tuna and Onion Ice-cream", "F003", "Vanilla.png",
                    "You know what you signed up for, and you wont regret it", 5000.00)

    pro4 = Products(104, "Empire Vanilla Ice-cream", "F004", "Vanilla.png",
                    "Regular Ice cream", 5000.00)

    d_list = [pro1, pro2, pro3, pro4]
    return d_list

def anum_gen():
    """
    Generates an auto incrementing ID. TEMPORARY UNTIL THE DATABASE IS ADJUSTED.
    """
    global START
    global END

    newAnum = START
    START = START+1

    if newAnum > END:
        return "No new Numbers"
    else:
        return newAnum

def is_new(userid, list):
    """
    Checks if the user was registered recently (if they have any predictions generated).
    """
    print(list)

    if userid not in list:
        return True
    else:
        return False

def fetch_recomm(type,uRList):
    """
    Fetches recommendation based on user type.
    """

    if type == 1:
        recomProd = []
        print(uRList)
        for i in uRList:
            recomProd.extend(Item.query.filter_by(i_type=i).all())

        print("List of items: \n")
        print(recomProd)
        return recomProd
    else:
        recomProd = []
        print(uRList[1])
        for i in uRList[1]:
            recomProd.append(Item.query.filter_by(item_id=i).first())

        print("List of items: \n")
        print(recomProd)
        return recomProd
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
