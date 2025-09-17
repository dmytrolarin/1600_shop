import flask_migrate
import flask_sqlalchemy
from .settings import project
import os
import sqlalchemy


project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db: sqlalchemy = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(
    app = project,
    db = db,
    directory= os.path.abspath(os.path.join(__file__, "..", "migrations"))
)