import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Add an if statement to conditionally set the database URI
if os.environ.get("DB_URL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    database_url = os.environ.get("DATABASE_URL")
    # Adjust the URL if it starts with "postgres://"
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url

db = SQLAlchemy(app)

from taskmanager import routes  # noqa Non quality assurance
