import flask, dotenv, os, requests
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

PATH_ENV = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
dotenv.load_dotenv(dotenv_path= PATH_ENV)

MONOBANK_TOKEN= dotenv.get_key("MONOBANK_TOKEN")
MONOBANK_API_URL= "https://api.monobank.ua/api/merchant/invoice/create"

def create_payment():
    product_id = flask.request.args.get('product_id') 
    product = Product.query.get(int(product_id))
    price = int(product.price)

    payload = { 
        "amount": price, 
        "ccy": 980,
        "redirectUrl": "http://127.0.0.1:5000/"
    }  

    headers = {"X-Token": MONOBANK_TOKEN}

    requests.post(MONOBANK_API_URL, json= payload, headers= headers )


    

