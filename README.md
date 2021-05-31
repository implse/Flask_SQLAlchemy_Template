# Flask SQLAlchemy Template

This is a simple app using Flask and Flask-SQLAlchemy library which is an extension wrapper for SQLAlchemy.

## What is SQLAlchemy?

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

SQLAlchemy abstract the database system, simplifying the interactions with the database.


## What is Flask-SQLAlchemy?

Flask-SQLAlchemy is an extension for Flask which adds support for the SQLAlchemy SQL toolkit/ORM (Object Relational Mapping).


## Configuration

- Create a project folder

- Create a virtual environment using the command:

    `python -m venv env`

- Clone the GitHub repo Flask SQLAlchemy Template:

    `git clone https://github.com/implse/Flask_SQLAlchemy_Template.git`

- Install requirements.txt :

    `pip install requirements.txt`

- Add your personal `SECRET KEY`

To enable communication with a database, the Flask-SQLAlchemy extension takes the location of the application’s database from the `SQLALCHEMY_DATABASE_URI`.

`SQLALCHEMY_TRACK_MODIFICATIONS` configuration option to `False` to disable a feature of Flask-SQLAlchemy that signals the application every time a change is about to be made in the database.

Next, we create an SQLAlchemy `object` and bind it to our `app`.

```
db = SQLAlchemy(app)

```
The database object `db` created contains all the functions and helpers from both SQLAlchemy and SQLAlchemy ORM.

## Model Definition

In the context of an ORM, a `model` is a Python `class` with attributes that
match the columns of a corresponding database `table`.

To create a `model` or table schema to your application, you need to create a `class` that inherits from `Model`.

```
class User(db.Model):
  ...

```


## Database Operations

The very first thing to do is to instruct Flask-SQLAlchemy to create a database based
on the model classes.

The `db.create_all()` function locates all the subclasses of `db.Model` and creates the corresponding tables in the database.

from the terminal launch `flask shell` or `python` then type the following commands:
  - Import the database instance `db` from `template.py`.
  - Create all database `tables` according to the `models`.

```
from template import db

db.create_all()

```

If you check the application directory, you will now see a new file there called `database_name.db`.


# SQLite

You can use the terminal to manage your database with SQLite.

launch `sqlite3` from the terminal.

```
.open database_name.db

.schema
````

### Add Users

```
INSERT INTO user (username, email) VALUES ("Dave Brubeck", "dave.brubeck@quartet.liv");
INSERT INTO user (username, email) VALUES ("Paul Desmond", "paul.desmond@quartet.liv");
INSERT INTO user (username, email) VALUES ("Joe Morello", "joe.morello@quartet.liv");
INSERT INTO user (username, email) VALUES ("Eugene Wright", "eugene.wright@quartet.liv");
```

### SQL commands

```
SELECT name, email FROM user;

```
