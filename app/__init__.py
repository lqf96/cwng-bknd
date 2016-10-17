# __init__.py: Website package entry point and initialization
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import config

# Flask application
app = Flask(__name__)
# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(os.getcwd(), config.DB_TEST_PATH)

# Database
db = SQLAlchemy(app)

# All packages to be imported in this project
from app import base
