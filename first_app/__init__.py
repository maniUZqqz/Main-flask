from first_app import views, models, error_pages, templates, static
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "mani"






if __name__ == '__main__':
    app.run(debug=True)