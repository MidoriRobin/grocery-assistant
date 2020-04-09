# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DeliversTo(Base):
    __tablename__ = 'delivers_to'

    deliv_id = Column(String(10), primary_key=True)
    d_type = Column(String(10))
    deliv_time = Column(String(10))


class Supermarket(Base):
    __tablename__ = 'supermarket'

    spm_id = Column(String(10), primary_key=True)
    spm_name = Column(String(60), index=True)
    street = Column(String(60))
    city = Column(String(50))
    branch = Column(String(60))


class Usr(Base):
    __tablename__ = 'usr'

    acc_num = Column(String(20), primary_key=True)
    fname = Column(String(20))
    lname = Column(String(20))
    sex = Column(CHAR(1))
    phone = Column(String(100))
    city = Column(String(100))
    street = Column(String(100))
    email = Column(String(100))
    hh_size = Column(INTEGER(11))
    no_adults = Column(INTEGER(11))
    no_kids = Column(INTEGER(11))
    marital_s = Column(CHAR(1))
    diet_pref = Column(String(20))


class Courier(Base):
    __tablename__ = 'courier'

    cour_id = Column(String(10), primary_key=True)
    cour_name = Column(String(100))
    spm_name = Column(ForeignKey('supermarket.spm_name', ondelete='CASCADE'), index=True)
    loc = Column(String(100))

    supermarket = relationship('Supermarket')


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(String(20), primary_key=True)
    item_name = Column(String(100))
    price = Column(String(10))
    brand = Column(String(30))
    desc_item = Column(String(100))
    i_type = Column(String(30))
    likes = Column(INTEGER(11))
    dislikes = Column(INTEGER(11))
    exp_date = Column(String(20))
    acc_num = Column(ForeignKey('usr.acc_num'), index=True)
    spm_id = Column(ForeignKey('supermarket.spm_id'), index=True)

    usr = relationship('Usr')
    spm = relationship('Supermarket')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String(20), primary_key=True)
    acc_num = Column(ForeignKey('usr.acc_num'), index=True)
    deliv_time = Column(String(100))
    sale_value = Column(DECIMAL(10, 2))

    usr = relationship('Usr')


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    cart_id = Column(String(20), primary_key=True)
    acc_num = Column(ForeignKey('usr.acc_num'), index=True)

    usr = relationship('Usr')


class Payment(Base):
    __tablename__ = 'payment'

    pay_id = Column(String(10), primary_key=True)
    order_id = Column(ForeignKey('orders.order_id', ondelete='CASCADE'), index=True)
    p_time = Column(String(10))

    order = relationship('Order')


class Review(Base):
    __tablename__ = 'review'

    acc_num = Column(ForeignKey('usr.acc_num'), primary_key=True, nullable=False)
    item_id = Column(ForeignKey('items.item_id'), primary_key=True, nullable=False, index=True)
    ratings = Column(Enum('1', '2', '3', '4', '5'))

    usr = relationship('Usr')
    item = relationship('Item')


class ShoppingList(Base):
    __tablename__ = 'shopping_list'

    list_id = Column(String(20), primary_key=True)
    item_id = Column(ForeignKey('items.item_id'), index=True)
    quantity = Column(String(20))

    item = relationship('Item')


class Usi(Base):
    __tablename__ = 'usi'

    acc_num = Column(ForeignKey('usr.acc_num'), primary_key=True, nullable=False)
    item_id = Column(ForeignKey('items.item_id'), primary_key=True, nullable=False, index=True)
    cart_id = Column(ForeignKey('shopping_cart.cart_id'), primary_key=True, nullable=False, index=True)

    usr = relationship('Usr')
    cart = relationship('ShoppingCart')
    item = relationship('Item')
