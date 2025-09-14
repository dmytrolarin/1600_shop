import flask 
import flask_migrate
import flask_sqlalchemy
from .settings import project

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'