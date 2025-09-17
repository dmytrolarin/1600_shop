from .urls import *
from .settings import project
from .db import *
from .loadenv import load_env
from shop.models import Product

project.register_blueprint(blueprint= shop.shop)