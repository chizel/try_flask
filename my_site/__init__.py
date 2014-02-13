from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('my_site.config')
db = SQLAlchemy(app)

from my_site import views, models
