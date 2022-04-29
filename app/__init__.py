from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

import os

from app.log import Log
from app.models import db
from app.routes import initialize_routes
from settings import DB_NAME, ROOT_PATH

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)
initialize_routes(app, api)
path_db = os.path.join(ROOT_PATH,DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path_db +'?check_same_thread=False'

db.init_app(app)
LOG = Log(__name__)

with app.app_context():
    # db.drop_all()
    db.create_all()

