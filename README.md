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


## Database Operations

The very first thing to do is to instruct Flask-SQLAlchemy to create a database based
on the model classes.

The `db.create_all()` function locates all the subclasses of `db.Model` and creates the corresponding tables in the database.

from the terminal launch `flask shell` or `python` then type the following commands.

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
