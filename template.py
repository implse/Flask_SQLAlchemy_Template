from flask import Flask
from sql_alchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy Global Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "YourSecretKey"

# Instantiate SQLAlchemy
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "<p>SQL Alchemy Template</p>"
