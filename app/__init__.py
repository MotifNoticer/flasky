from flask import Flask
# import SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy
# import migreate
from flask_migrate import Migrate

# instantiate db and instantiate migrate
# gives us access to database operations
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    # set up the database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'

    # connect the db and migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    # import routes
    from .routes import crystal_bp
    # register the blueprint
    app.register_blueprint(crystal_bp)
    from app.models.crystals import Crystal
    
    return app

    