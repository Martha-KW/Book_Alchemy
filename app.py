from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# If you want to run the app
if __name__ == '__main__':
    app.run(debug=True)
