from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
