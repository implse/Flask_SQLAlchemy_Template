from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy Global Configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#timeouts
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "YourSecretKey"

# The db object instantiated from the class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

# Model Definition : Python class with attributes that match the columns of the corresponding database table
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def index():
    return "<h2>You have just created your first Flask application supporting databases!</h2>"
