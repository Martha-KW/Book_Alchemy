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

# route for the homepage
@app.route('/')
def home():
    books = Book.query.all()  # get all books from database
    return render_template('home.html', books=books)



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


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    message = ""
    authors = Author.query.all()

    if request.method == 'POST':
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        try:
            new_book = Book(
                title=title,
                isbn=isbn,
                publication_year=int(publication_year) if publication_year else None,
                author_id=int(author_id)
            )
            db.session.add(new_book)
            db.session.commit()
            message = f"Book '{title}' successfully added!"
        except Exception as e:
            db.session.rollback()
            message = f"Error adding book: {e}"

    return render_template('add_book.html', authors=authors, message=message)



# creates the tables, first time use only, reactivate if needed
# with app.app_context():
#     db.create_all()

print("working directory:", os.getcwd())
# If you want to run the app
if __name__ == '__main__':
    app.run(debug=True)
