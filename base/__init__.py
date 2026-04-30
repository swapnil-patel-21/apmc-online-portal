import os
import warnings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

app = Flask(__name__)

app.secret_key = 'sessionData'

# app.config['SQLALCHEMY_ECHO']= True

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)

import base.com.controller
from base.com.controller import dashboard_controller