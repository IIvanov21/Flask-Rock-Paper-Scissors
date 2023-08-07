from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
app.config['SECRET_KEY'] = secrets.token_hex(8)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()
db = SQLAlchemy(app)

from application import routes