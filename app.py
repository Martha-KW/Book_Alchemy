from data_models import db, Author, Book
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
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


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        birth_date_str = request.form.get('birth_date')
        date_of_death_str = request.form.get('date_of_death')

        # convert the date strings to  datetime.date
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date() if birth_date_str else None
        date_of_death = datetime.strptime(date_of_death_str, '%Y-%m-%d').date() if date_of_death_str else None

        new_author = Author(
            name=name,
            birth_date=birth_date,
            date_of_death=date_of_death
        )
        try:
            db.session.add(new_author)
            db.session.commit()
            message = f"Author '{name}' successfully added to database!"
        except Exception as e:
            db.session.rollback()
            message = f"Error adding author: {str(e)}"

    return render_template('add_author.html', message=message)



# creates the tables, only one time needed
# with app.app_context():
#   db.create_all()

print("working directory:", os.getcwd())
# If you want to run the app
if __name__ == '__main__':
    app.run(debug=True)
