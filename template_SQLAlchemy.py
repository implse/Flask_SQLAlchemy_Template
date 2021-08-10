from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy Global Configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "YourSecretKey"

# The db object instantiated from the class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

# Model Definition : Python class with attributes that match the columns of the corresponding database table
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class Musicien(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    birthdate = db.Column(db.Text(80), nullable=False)
    instruments = db.Column(db.Text(80), nullable=False)
    genre = db.Column(db.Text(80), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.birthdate}, {self.instruments}, {self.genre}"

@app.route("/")
def index():
    return "<h2>You have just created your first Flask application supporting databases!</h2>"

if __name__ == '__main__':
   app.run(debug = True)
