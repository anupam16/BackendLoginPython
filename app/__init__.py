from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import Config
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)

from app import models, resources
