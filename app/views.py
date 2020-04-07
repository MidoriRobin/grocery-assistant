"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import *
from werkzeug.security import check_password_hash
import random


###
# Routing for application.
###

@app.route('/')
def home():
    """Render website's home page."""
    products = Products.query.filter_by().all()
    return render_template('home.html',products=products)


@app.route('/about/')
def about():
    """Render the website's about page."""
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


            user = UserProfile.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password, password):
                login_user(user)

            return redirect(url_for('secure_page'))
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))


#@app.route('/products')
#def products():
    #rows = Products.query.filter_by().all()
    #return render_template('products.html', prods=rows)
    #pass
###

#The route can be changed to "TryThese" instead of "Recommended items"
@app.route('/recommended items')
def recomm():
    """Renders the recommendation page for a specific user based on the
        items they previously rated."""

    products = Products.query.filter_by().all()

# Dummy recommendations
    buylst = dummyList()

# Getting the list of recommended products, using the predictions(INCOMPLETE)
    #p_list = Products.query.filter_by()
# Function to randomize
    rprop = buylst + rdmizePredictions(products)
    return render_template('recommendation.html', recom=rprop)

def rdmizePredictions(product_list):
    """
    Fetches, six random products from a list of predictions.
    """
    six_rand_prod = []
    r_num = len(pList)

    while len(six_rand_prod) < 6:
        prod = products[random.randrange(0,r_num)]
        if prod in pList:
            continue
        else:
            six_rand_prod.append(prod)
    return six_rand_prod

def dummyList():
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
