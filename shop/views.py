import flask
from .models import Product


def render_catalog():
    
    list_products = Product.query.all()     
    return flask.render_template(
        template_name_or_list="catalog.html",
        list_products=list_products
        )