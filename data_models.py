from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __str__(self):
        return f"{self.name} ({self.birth_date} - {self.date_of_death})"

    def __repr__(self):
        return f"<Author id={self.id} name='{self.name}'>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    # Optional: define relationship (if needed later)
    author = db.relationship('Author', backref='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    def __repr__(self):
        return f"<Book id={self.id} title='{self.title}' isbn='{self.isbn}'>"
