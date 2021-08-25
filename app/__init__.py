from flask import Flask
from flask_mail import Mail
from app import config

app = Flask(__name__)
app.config.from_object(config.Config)
mail = Mail(app)

from app import routes
