import flask
from .models import Product


def render_catalog():
    list_products = Product.query.all()  

    if flask.request.method == 'POST':
        category = flask.request.form.get("category")

        if category != "all":
            list_products = Product.query.filter_by(category = category) 



    return flask.render_template(
        template_name_or_list="catalog.html",
        list_products=list_products
        )