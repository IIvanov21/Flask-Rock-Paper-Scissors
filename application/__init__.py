from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import secrets
from decouple import config
from application.classes import RockPaperScissors

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(8)

from application import routes