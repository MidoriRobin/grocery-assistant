"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from flask_cors import cross_origin

from app.forms import *
from app.models import *
from werkzeug.security import check_password_hash
import random
from datetime import date
from decimal import *

from app.RecomHandler import RecomHandler
from app.Cbrec2 import cbrec2

###
# Routing for application.
###


#api routes

@app.route('/')
def home():
    """Render website's home page."""
    products = Products.query.filter_by().all()
    return render_template('home.html',products=products)

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/api/ping')
def ping():

    message = "New Ping"
    return jsonify(message=message)

@app.route('/about/')
def about():
    """Render the website's about page."""

    # product = ShoppingCart.query.filter_by(acc_num=1323).order_by(ShoppingCart.cart_id.desc()).first()
    # product = Item.query.filter_by(item_id=1).first()
    # person = ShoppingCart.query.filter_by(acc_num=1323).first()
    # print(person.__dict__)

    # Use this to posibly suggest items a user can possibly review
    result = RecomHandler.collab_fltr(1323,24028)
    # result2 = cbrec2()

    print(result)
    cart = ShoppingCart.query.filter_by(acc_num=1323).first()
    print(cart.sum_items())
    # print(RecomHandler.cont_fltr())

    return render_template('about.html')


@app.route('/secure-page')
@login_required
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')


@app.route('/api/login', methods=['POST'])
def login():
    form = LoginForm()
    #and form.validate_on_submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if int(username) in range(1234,1333):
            print("this is a test user..")
            user = Usr.query.filter_by(acc_num=username).first()
            if user is not None and user.password == password:
                login_user(user)
                print("User logged in")
                session['cartid'] = user.get_cartid()
                status = {
                    "message": "User successfully logged in",
                    "userid": user.acc_num,
                    "cartid": user.get_cartid()
                }
            else:
                status = {
                    "message": "Invalid password or no such user exists"
                }

        elif int(username) >= 1333:
            print("not a test user..")
            user = Usr.query.filter_by(acc_num=username).first()
            if user is not None and check_password_hash(user.password, password):
                login_user(user)
                session['cartid'] = user.get_cartid()
                status = {
                    "message": "User successfully logged in",
                    "userid": user.acc_num,
                    "cartid": user.get_cartid()
                }
            else:
                status = {
                    "message": "Invalid password or no such user exists"
                }
        else:
            status = {
                "message": "Error in login attempt",
                "errors": [
                    form_errors(form)
                ]
            }

    return jsonify(status=status)

@app.route('/api/logout', methods=['GET'])
# @login_required
def logout():
    session.pop('logged_in', None)
    session.pop('cartid', None)
    logout_user()
    flash('You were logged out', 'success')

    status = {
        "message": "User logged out"
    }

    # return redirect(url_for('home'))
    return jsonify(status=status)

#User sign up route
@app.route('/api/signup', methods=['GET','POST'])
def signup():
    form = UsrForm()
    #Collect data from form and save in database
    if request.method == 'POST':
        fname= request.form['firstname']
        lname= request.form['lastname']
        sex = request.form['gender']
        email= request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        street = request.form['street']
        hh_size = request.form['hhsize']
        no_adults = request.form['adlts']
        no_kids = request.form['kids']
        marital_s = request.form['maritalstat']
        diet_pref = request.form['dietpref']
        password = request.form['password']


        user = Usr(fname,lname,sex,phone,city,street, email, hh_size,
        no_adults,no_kids,marital_s,diet_pref,password)
        db.session.add(user)
        db.session.commit()


        flash('success','')

        status = {
            "message": "user successfully signed up"
        }

    else:
        status = {
            "message": "Error in signup",
            "errors": form_errors(form)
        }
        # return redirect(url_for('home'))
    # return render_template('signup.html', form=form)

    return jsonify(status=status), 201


@login_manager.user_loader
def load_user(id):
    return Usr.query.get(id)


@app.route('/api/products', methods=['GET'])
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

    # return render_template('products.html', prods=rows, prodos=prodos.items, next=next_url, prev = prev_url)

    status = {
        "current_page": page,
        "prev_page": prodos.prev_num,
        "next_page": prodos.next_num,
        "total_pages": prodos.pages,
        "products": [product.to_dict() for product in prodos.items],
    }

    return jsonify(status=status), 201


@app.route('/api/products/<itemid>', methods=['GET'])
def product(itemid):
    list = []
    revform = ReviewForm()
    listform = ItemListForm()
    # list = RecomHandler.cont_bsd_fltr(1)
    print(list)
    item = Item.query.filter_by(item_id=itemid).first()

    if current_user.is_active:
        slists = ShoppingList.query.filter_by(acc_num=current_user.acc_num).all()
        listform.listname.choices = [(list.list_id, list.name) for list in slists]
    else:
        slists = []

    flash("Displaying product")

    status = {
        "message": "Successfully fetched item",
        "item": item.to_dict(),
        "userlists": [list.to_dict() for list in slists if list != []]
    }

    # return render_template('/test-templates/product.html', item=item, revform=revform, listform=listform)

    return jsonify(status=status), 201

@app.route('/api/products/<itemid>/<userid>', methods=['GET'])
def eval_product(itemid,userid):
    """
    Accepts the users id and item id and runs a check to see whether the user
    in question would like the item based on the recommendation model
    """

    message = "No message"
    items = []

    userid = int(userid)
    itemid = int(itemid)

    recInfo = RecomHandler.collab_fltr(userid,itemid)
    print("UserId:", recInfo.uid)
    print("ItemId:", recInfo.iid)
    rating = Decimal.from_float(round(recInfo.est,2))
    print("Estimated rating:", rating)

    if rating >= 3.0:
        message = "You should try this item"
    elif rating < 3.0 and rating >= 2.5:
        message = "You might like this item"
    elif rating < 2.5:
        message = "You probably wont like this item"
        item = Item.query.filter_by(item_id=itemid).first()
        ptntialItems = Item.query.filter_by(i_type=item.i_type).limit(50).all()

        items = [item for item in ptntialItems if (RecomHandler.collab_fltr(userid,item.item_id).est > 2.5) ]

    status = {
        "message": message,
        "items": [item.to_dict() for item in items[:3]]
    }

    return jsonify(status=status), 201
#The route can be changed to "TryThese" instead of "Recommended items"
@app.route('/api/TryThese/<userid>', methods=['GET'])
# @login_required
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
    # randPred = rdmize_predictions(recomProd)
    randPred = recomProd

    print(randPred)

    status = {
        "message": "Recommended items obtained",
        "items": [item.to_dict() for item in randPred]
    }

    # return render_template('recommendation.html', recom=randPred)
    return jsonify(status=status), 201

@app.route('/api/TryThese/<userid>/<categr>', methods=['GET'])
def fltr_recomm(userid, categr):

# Prepares recommendations, compiles products in an array
    recomD = RecomHandler.recomHelper()
    cUser = Usr.query.filter_by(acc_num=userid).first()
    trueCat = int(categr) - 1
# If statement to check if the user is a new user and has any previous recommendation
    if is_new(userid, recomD["uid"]):
        print("New user!")
        uRecom = RecomHandler.diet_cnvrtr(pref=None, typecode=trueCat)
        recomProd = fetch_recomm(1,uRecom)
    else:
        print("Old user..")
        type = RecomHandler.diet_cnvrtr(pref=None, typecode=trueCat)
        uRecom = RecomHandler.rec_by_usr(userid, recomD)
        recomProd = fetch_recomm(2,uRecom,dtype=type)

    randPred = rdmize_predictions(recomProd)
    print(randPred)

    if randPred is None:

        status = {
            "message": "No items available",
            "items":[]
        }

    else:
        status = {
            "message": "Recommended items obtained",
            "items": [item.to_dict() for item in randPred]
        }

    return jsonify(status=status), 201

#Cart----------------------------------------------
@app.route('/api/users/<userid>/cart', methods=['GET'])
# @login_required
def cart(userid):
    """View items in users cart"""

    #Fetching the users shopping cart ID
    cart = ShoppingCart.query.filter_by(acc_num=userid).order_by(ShoppingCart.cart_id.desc()).first()

    itemList = cart.fetch_all_items()

    status = {
    "message": "cart successfully fetched",
    "cart": itemList,
    "total_cost": str(cart.sum_items())
    }

    flash("cart successfully fetched")
    # return render_template('/test-templates/cart.html', list=itemList)

    return jsonify(status=status)

@app.route('/api/items/<itemid>/<qty>/cart/<cartid>', methods=['POST'])
# @login_required
def add_item_cart(itemid,qty, cartid):
    """Route to add item to a cart"""

    item = Usi(cartid, itemid, qty, date.today())
    db.session.add(item)
    db.session.commit()

    item = Item.query.filter_by(item_id=itemid).first()

    status = {
        "message": "item successfully added to cart",
        "item": item.item_name,
        "description": item.desc_item
    }

    print(status)
    flash("item successfully added to cart")
    # return redirect(url_for('products'))

    return jsonify(status=status), 201

@app.route('/api/users/<userid>/cart/<cartid>/<itemid>', methods=['DELETE'])
# @login_required
def remove_from_cart(userid,itemid,cartid):
    item = Usi.query.filter_by(cart_id=cartid,item_id=itemid).first()

    db.session.delete(item)
    db.session.commit()

    status = {
        "message": "Item removed from cart successfully",
        "item": Item.query.filter_by(item_id=itemid).first().to_dict()
    }

    flash("Item deleted successfully")
    # return status
    # return redirect(url_for('cart', userid=current_user.acc_num))
    return jsonify(status=status), 201

#Lists----------------------------------------------
@app.route('/api/users/<userid>/lists', methods=['POST'])
# @login_required
def make_list(userid):
    """Route to add a new list to a user account"""

    if request.method == 'POST':
        list = ShoppingList(userid, request.form['name'], date.today())

        db.session.add(list)
        db.session.commit()

    status = {
        "messsage": "List successfully created",
        "list": request.form['name']
    }

    flash("List successfully created")
    # return status
    # return redirect(url_for('view_lists'))
    return jsonify(status=status)

@app.route('/api/users/<userid>/lists', methods=['GET'])
# @login_required
def view_lists(userid):
    """Route to view all lists of a specific user"""

    lists = ShoppingList.query.filter_by(acc_num=userid).all()

    status = {
        "Message": "Displaying all shopping lists based on user id",
        "lists": [list.to_dict() for list in lists]
    }

    flash("Displaying all shopping lists based on user id")
    #return status
    # return render_template('/test-templates/lists.html', LoL=lists)
    return jsonify(status=status), 201

@app.route('/api/users/<userid>/lists/<listid>', methods=['GET'])
# @login_required
def list(userid,listid):
    """Route to view a list of a specific user"""

    list = ShoppingList.query.filter_by(list_id=listid).first()
    items = list.view_items()
    status = {
        "message": "Displaying all items in the shopping list chosen",
        "list": list.to_dict(),
        "items": items
    }

    flash("Displaying all items in the shopping list chosen")
    #return status
    # return render_template('/test-templates/list.html', items=items, list=list)
    return jsonify(status=status)

@app.route('/api/items/<itemid>/lists/', methods=['POST'])
# @login_required
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

    status = {
        "message": "Item added to list",
        "item": Item.query.filter_by(item_id=itemid).first().to_dict()
    }

    flash("Item added to list")
    # return status
    # return redirect(url_for('product',itemid=itemid))
    return jsonify(status=status)

@app.route('/api/users/lists/<listid>/<itemid>', methods=['DELETE'])
# @login_required
def remove_from_list(listid,itemid):

    item = ListItem.query.filter_by(list_id=listid, item_id=itemid).first()

    db.session.delete(item)
    db.session.commit()

    status = {
        "message": "Item successfully removed from list",
        "item": Item.query.filter_by(item_id=itemid).first().to_dict()
    }

    flash("Item successfully deleted")
    # return status
    # return redirect(url_for('list', listid=listid, userid=current_user.acc_num))
    return jsonify(status=status), 201

@app.route('/api/users/<userid>/lists/<listid>', methods=['DELETE'])
def delete_list(listid):

    list = ShoppingList.query.filter_by(list_id=listid).first()

    db.session.delete(list)
    db.session.commit()

    status = {
        "message": "List deleted successfully"
    }

    return jsonify(status=status), 201

#Courier----------------------------------------------
@app.route('/courier', methods=['GET'])
def courier(arg):
    """Shows a list of couriers"""
    pass


#Order----------------------------------------------
@app.route('/api/users/<userid>/orders/', methods=['GET'])
def orders(userid):

    orders = Order.query.filter_by(acc_num=userid).order_by(Order.order_id.desc()).all()

    status = {
        "message": "Orders successfully fetched",
        "orders": [order.to_dict() for order in orders]
    }


    return jsonify(status=status), 201

@app.route('/api/users/<userid>/orders/<orderid>', methods=['GET'])
def order(userid,orderid):
    print("fetching order")
    order = Order.query.filter_by(order_id=orderid).first()

    cart = ShoppingCart.query.filter_by(cart_id=order.cart_id).first()
    status = {
        "message": "Order obtained",
        "order": order.to_dict(),
        "cart": cart.to_dict(),
        "items": cart.fetch_all_items()
    }

    return jsonify(status=status), 201

@app.route('/api/users/<userid>/cart/<cartid>/orders', methods=['POST'])
def make_order(userid,cartid):
    #IMplement simulated order cart-table > order-table
    cart = ShoppingCart.query.filter_by(cart_id=cartid).first()

    order = Order(userid,cartid,date.today(), cart.sum_items())
    db.session.add(order)
    db.session.commit()


    new_cart = ShoppingCart(userid, date.today())

    db.session.add(new_cart)
    db.session.commit()

    status = {
    "message": "Order placed successfully",
    "cartid": Usr.query.filter_by(acc_num=userid).first().get_cartid()
    }

    return jsonify(status=status), 201

#Review----------------------------------------------

@app.route('/api/items/<itemid>/review/', methods=['POST'])
def review_item(itemid):

    if request.method == 'POST':
        rCheck = Review.query.filter_by(acc_num=request.form['userid'], item_id=itemid).first()

        if rCheck:
            rCheck.rating = request.form['rating']
        else:
            review = Review(request.form['userid'],itemid,request.form['rating'])
            db.session.add(review)

    db.session.commit()

    status = {
        "message": "Review successfully added",
        "rating": request.form['rating']
    }

    flash("Review successfully added")
    # return status
    # return redirect(url_for('products',itemid=itemid))
    return jsonify(status=status)

@app.route('/api/items/<itemid>/review/', methods=['GET'])
def get_reviews(itemid):

    reviews = Review.query.filter_by(item_id=itemid).all()

    status = {
        "message": "Reviews fetched sucessfully",
        "reviews": [review.to_dict() for review in reviews]
    }

    return jsonify(status=status), 201

#Locally required functions

def rdmize_predictions(product_list):
    """
    Fetches, six random products from a list of predictions.
    """
    six_rand_prod = []
    r_num = len(product_list)
    print(r_num)

    if r_num == 0:
        return None
    elif r_num < 6:
        print("Not many products so returning list..")
        return product_list
    else:
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

def fetch_recomm(type,uRList,dtype=None):
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

    elif dtype:
        print("regenerating recommendations based on item type")
        recomProd = []
        print(uRList)
        for i in uRList[1]:
            for type in dtype:
                item = Item.query.filter_by(item_id=i, i_type=type).first()
                if item is not None:
                    recomProd.append(item)
                else:
                    continue

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
    app.run(debug=True,host="0.0.0.0",port="5000")
