# third-party imports
import os
from flask import Flask
from flask_mongoengine import MongoEngine

# local imports
from app.models import *
from config import Config


CURRENT_WORKING_DIRECTORY = os.getcwd()


db = MongoEngine()




def create_app():
    app = Flask(__name__, instance_relative_config=True, root_path=os.path.join(CURRENT_WORKING_DIRECTORY, 'app'))
    app.config.from_object(Config)
    
    db.init_app(app)

    from app.routes import blueprints

    for route_blueprint in blueprints:
        app.register_blueprint(route_blueprint, url_prefix='/api/v1/audio_management')
        
    return app
