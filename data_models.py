from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Author(db.Model):
    """The author class is responsible for the author table with the columns id (
    auto incremented), (author) name, birthdate and optional death date.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __str__(self):
        return f"{self.name} ({self.birth_date} - {self.date_of_death})"

    def __repr__(self):
        return f"<Author id={self.id} name='{self.name}'>"

class Book(db.Model):
    """The book class is responsible for the book table that contains an auto incremented
    book id, ISBN to fetch the cover image, the book title, the year of the
    publication, and an author id that corresponds as a foreign key with the id in the
     author table.
     """
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    # Optional: define relationship (if needed later)
    author = db.relationship('Author', backref='books')

    def __str__(self):
        # returns a human readable string for display purposes in frontend and cli
        return f"{self.title} ({self.publication_year})"

    def __repr__(self):
        # returns a string that is useful for debugging
        return f"<Book id={self.id} title='{self.title}' isbn='{self.isbn}'>"
