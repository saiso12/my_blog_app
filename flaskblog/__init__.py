from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "0e1d69604f9e7bcde06a39ef3afc18e6"
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes