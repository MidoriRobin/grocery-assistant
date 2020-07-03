from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username

class Products(db.Model):
    """docstring forProducts."""

    __tablename__ = 'catalog'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
    image = db.Column(db.String(80))
    desc = db.Column(db.Text)
    price = db.Column(db.Float)

    def __init__(self, pid, name, code, image, desc, price):
        self.pid = pid
        self.name = name
        self.code = code
        self.image = image
        self.desc = desc
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_img(self, arg):
        return self.image

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Item %s $ %s>' %  self.name,self.price

##########################################################

class DeliversTo(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'delivers_to'

    deliv_id = db.Column(db.Integer, primary_key=True)
    d_type = db.Column(db.String(10))
    deliv_time = db.Column(db.String(10))

    def __init__(self, arg):
        pass


class Supermarket(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'supermarket'

    spm_id = db.Column(db.Integer, primary_key=True)
    spm_name = db.Column(db.String(60), unique=True, index=True)
    street = db.Column(db.String(60))
    city = db.Column(db.String(50))
    branch = db.Column(db.String(60))

#Usr Model to be put back here
class Usr(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'usr'

    #This will be changed back to strinn temporarily
    acc_num = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    sex = db.Column(db.String(6))
    phone = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    email = db.Column(db.String(100))
    hh_size = db.Column(db.String(6))
    no_adults = db.Column(db.String(6))
    no_kids = db.Column(db.String(6))
    marital_s = db.Column(db.String(10))
    diet_pref = db.Column(db.String(20))
    password = db.Column(db.String(255))

    def __init__(self, fname, lname, sex, phone, city, street, email, hh_size, no_adults, no_kids, marital_s, diet_pref, password):

        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.phone = phone
        self.city = city
        self.street = street
        self.email = email
        self.hh_size = hh_size
        self.no_adults = no_adults
        self.no_kids = no_kids
        self.marital_s = marital_s
        self.diet_pref = diet_pref
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def get_cartid(self):

        cart = ShoppingCart.query.filter_by(acc_num=self.acc_num).order_by(ShoppingCart.cart_id.desc()).first()

        return cart.cart_id

    def get_lists(self):
        lists = ShoppingList.query.filter_by(acc_num=self.acc_num).all()

        return lists

    def to_dict(self):

        dict = {
            "fname": self.fname,
            "lname": self.lname,
            "sex": self.sex,
            "phone": self.phone,
            "city": self.city,
            "street": self.street,
            "email": self.email,
            "hh_size": self.no_adults,
            "no_kids": self.no_kids,
            "martial_s": self.martial_s,
            "diet_pref": self.diet_pref
        }

        return dict

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.acc_num)  # python 2 support
        except NameError:
            return str(self.acc_num)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.fname


class Courier(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'courier'

    cour_id = db.Column(db.Integer, primary_key=True)
    cour_name = db.Column(db.String(100))
    spm_name = db.Column(db.ForeignKey('supermarket.spm_name', ondelete='CASCADE'), unique=True, index=True)
    location = db.Column(db.String(100))

    supermarket = relationship('Supermarket')

    def __init__(self, cour_name, spm_name, loc):
        self.cour_name = cour_name
        self.spm_name = spm_name
        self.location = loc

    def to_dict(self):

        dict = {}

        pass


class Item(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    cost = db.Column(DECIMAL(10, 2))
    department = db.Column(db.String(50))
    brand = db.Column(db.String(30))
    desc_item = db.Column(db.String(255))
    i_type = db.Column(db.String(30))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    exp_date = db.Column(db.String(20))
    spm_id = db.Column(db.ForeignKey('supermarket.spm_id'), index=True)
    size = db.Column(db.String(25))

    spm = relationship('Supermarket')

    def __init__(self, item_name, price, brand, desc, type, exp, spm_id):

        self.item_name = item_name
        self.cost = price
        self.brand = brand
        self.desc_item = desc
        self.i_type = type
        self.exp_date = exp
        self.spm_id = spm_id

    def to_dict(self):

        dict = {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "cost": str(self.cost),
            "department": self.department,
            "brand": self.brand,
            "desc_item": self.desc_item,
            "i_type": self.i_type,
            "likes": self.likes,
            "dislikes": self.dislikes,
            "exp_date": self.exp_date,
            "size": self.size
        }

        return dict

    def __repr__(self):
        return '<Item: %s $ %s>' %  (self.item_name,self.cost)


class Order(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.ForeignKey('shopping_cart.cart_id'), index=True)
    acc_num = db.Column(db.ForeignKey('usr.acc_num'), index=True)
    date_ordered = db.Column(db.DateTime)
    deliv_time = db.Column(db.String(100))
    sale_value = db.Column(DECIMAL(10, 2))

    usr = relationship('Usr')
    cart = relationship('ShoppingCart')

    def __init__(self, acc_num, cartid, date_order, cost, deliv_time="N/A"):
        self.acc_num = acc_num
        self.cart_id = cartid
        self.deliv_id = deliv_time
        self.sale_value = cost
        self.date_ordered = date_order

    def fetch_items(self):

        cart = ShoppingCart.query.filter_by(cart_id=cart_id).first()

        return cart.fetch_all_items()

    def to_dict(self):

        dict = {
            "orderid": self.order_id,
            "acc_num": self.acc_num,
            "cartid": self.cart_id,
            "deliv_id": self.deliv_id,
            "sale_value": self.sale_value,
            "date_ordered": self.date_ordered,
            "no_items": len(self.fetch_items())
        }

        return dict


class ShoppingCart(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'shopping_cart'

    cart_id = db.Column(db.Integer, primary_key=True)
    acc_num = db.Column(db.ForeignKey('usr.acc_num'), index=True)
    date_created = db.Column(db.DateTime)

    usr = relationship('Usr')

    def __init__(self, acc_num, date_created):
        this.acc_num = acc_num
        this.date_created = date_created

    def to_dict(self):

        dict = {
            "cart_id": self.cart_id,
            "acc_num": self.acc_num,
            "date_created": self.date_created
        }

        return dict

    def fetch_all_items(self):

        cart_items = Usi.query.filter_by(cart_id=self.cart_id).all()
        print(cart_items)
        items = [cart_item.to_dict() for cart_item in cart_items]

        return items

    # Untested
    def sum_items(self):
        sumItems = 0

        items = [Item.query.filter_by(item_id=usiItem.item_id).first() for usiItem in Usi.query.filter_by(cart_id=self.cart_id).all()]
        print(items)
        sumItems = round(sum([item.cost for item in items]),2)

        return sumItems

    def add_to_cart(self, itemid, date, quantity=1):
        pass


class Payment(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'payment'

    pay_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey('orders.order_id', ondelete='CASCADE'), index=True)
    p_time = db.Column(db.String(10))

    order = relationship('Order')


class Review(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'review'

    acc_num = db.Column(db.ForeignKey('usr.acc_num'), primary_key=True, nullable=False)
    item_id = db.Column(db.ForeignKey('items.item_id'), primary_key=True, nullable=False, index=True)
    rating_desc = db.Column(db.Text)
    ratings = db.Column(db.Enum('1', '2', '3', '4', '5', name='rating_levels'))

    usr = relationship('Usr')
    item = relationship('Item')

    def __init__(self, userid, itemid, rating):

        self.acc_num = userid
        self.item_id = itemid
        self.ratings = rating

    def to_dict(self):

        dict = {
            "acc_num": self.acc_num,
            "item_id": self.item_id,
            "rating": self.rating
        }

        return dict


class ShoppingList(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'shopping_list'

    list_id = db.Column(db.Integer, primary_key=True)
    acc_num = db.Column(db.ForeignKey('usr.acc_num'), primary_key=True, index=True)
    name = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)

    usr = relationship('Usr')

    def __init__(self, acc_num, name, date_created):
        self.acc_num = acc_num
        self.name = name
        self.date_created = date_created

    def add_item(self, itemid, date, quantity=1):

        newItem = ListItem(self.list_id, itemid, date, quantity)

        db.session.add(newItem)
        db.session.commit()

        status = [{
            "message": "Item successfully added to list"
        }]

        return status

    def view_items(self):

        items = ListItem.query.filter_by(list_id=self.list_id).all()

        list_items = [item.to_dict() for item in items]


        return list_items

    def remove_item(self, itemid):

        item = ListItem.query.filter_by(list_id=self.list_id, item_id=itemid).first()

        db.session.delete(item)
        db.session.commit()

        status = [{
            "message": "Item successfully removed"
        }]

        return status

    def to_dict(self):

        dict = {
            "list_id": self.list_id,
            "acc_num": self.acc_num,
            "name": self.name,
            "date_created": self.date_created
        }

        return dict

    def __repr__(self):
        return '<List name %r ID: %r>' %  (self.name, self.list_id)


class ListItem(db.Model):
    """docstring for ListItem."""

    __bind_key__ = 'cpstnpro'
    __tablename__ = 'list_items'

    list_id = db.Column(db.ForeignKey('shopping_list.list_id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('items.item_id'), primary_key=True, nullable=False, index=True)
    quantity = db.Column(db.Integer, default=1)
    date_added = db.Column(db.DateTime)

    item = relationship('Item')
    list = relationship('ShoppingList')

    def __init__(self, list_id, item_id, date_added, quantity=1):
        self.list_id = list_id
        self.item_id = item_id
        self.date_added = date_added
        self.quantity = quantity

    def to_dict(self):

        dict = {
            "list_id": self.list_id,
            "item_id": self.item_id,
            "quantity": self.quantity,
            "date_added": self.date_added,
            "Item": self.fetch_item().to_dict()
        }

        return dict

    def fetch_item(self):
        return Item.query.filter_by(item_id=self.item_id).first()


class Usi(db.Model):
    __bind_key__ = 'cpstnpro'
    __tablename__ = 'usi'

    cart_id = db.Column(db.ForeignKey('shopping_cart.cart_id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('items.item_id'), primary_key=True, nullable=False, index=True)
    quantity = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)

    cart = relationship('ShoppingCart')
    item = relationship('Item')

    def __init__(self, cart_id, item_id, quantity, created_date):
        self.cart_id = cart_id
        self.item_id = item_id
        self.quantity = quantity
        self.created_date = created_date

    def fetch_item(self):
        return Item.query.filter_by(item_id=self.item_id).first()

    def to_dict(self):

        dict = {
            "cart_id": self.cart_id,
            "item_id": self.item_id,
            "quantity": self.quantity,
            "created_date": self.created_date,
            "Item": self.fetch_item().to_dict()
        }

        return dict
