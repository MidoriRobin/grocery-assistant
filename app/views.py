"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, UsrForm
from app.models import *
from werkzeug.security import check_password_hash
import random
from app.RecomHandler import RecomHandler

###
# Routing for application.
###

START = 1335
END = 1434

@app.route('/')
def home():
    """Render website's home page."""
    products = Products.query.filter_by().all()
    return render_template('home.html',products=products)


@app.route('/api/ping')
def ping():

    message = "New Ping"
    return jsonify(message=message)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/secure-page')
@login_required
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')


@app.route('/api/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    #and form.validate_on_submit():
    if request.method == 'POST':
        if form.username.data:
            username = form.username.data
            password = form.password.data


            user = Usr.query.filter_by(acc_num=username).first()
            if user is not None and check_password_hash(user.password, password):
                login_user(user)

                status = {
                    "message":"User sucessfully logged in"
                }

            #return redirect(url_for('secure_page'))

            else:
                status = {
                    "message":"User login unsucessful"
                }

    return jsonify(status=status)


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

        anum = anum_gen()
        user = Usr(anum,fname,lname,sex,email,phone,city,street,hh_size,
        no_adults,no_kids,marital_s,diet_pref,password)
        db.session.add(user)
        db.session.commit()

        flash('success','')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)



@login_manager.user_loader
def load_user(id):
    return Usr.query.get(id)


#@app.route('/products')
#def products():
    #rows = Products.query.filter_by().all()
    #return render_template('products.html', prods=rows)
    #pass
###

#The route can be changed to "TryThese" instead of "Recommended items"
@app.route('/TryThese/<userid>')
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
    if is_new(cUser.acc_num, recomD["uid"]):
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
    app.run(debug=True,host="0.0.0.0",port="5000")
