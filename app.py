from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book


# Create an instance of the Flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define the route for the homepage
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# If you want to run the app
if __name__ == '__main__':
    app.run(debug=True)
