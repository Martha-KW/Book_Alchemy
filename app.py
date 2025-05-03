from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import os


# Create an instance of the Flask application
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'library.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
print("SQLite-Pfad:", os.path.join(basedir, 'data', 'library.sqlite'))

# Define the route for the homepage
@app.route('/')
def home():
    return "Welcome to the Home Page!"

with app.app_context():
  db.create_all()

print("working directory: os.getcwd())")
# If you want to run the app
if __name__ == '__main__':
    app.run(debug=True)
