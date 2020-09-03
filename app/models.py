from app import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    author = db.Column(db.String(200), index=True)
    borrowed = db.relationship('Borrowed', backref = 'book', uselist=False)

    def __str__(self):
        return f"<Book {self.title}>"


class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrowed_date = db.Column(db.Date, index=True, default=datetime.today())
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Borrowed {self.id} {self.book_id}>"


# ------------

def add_book(book_form):
    new_title = book_form.data["title"]
    new_author = book_form.data["author"]
    new_book = Book(title=new_title, author=new_author)
    db.session.add(new_book)
    db.session.commit()

def borrow_book(book_title):
    book = Book.query.filter_by(title=book_title).first()
    borrowed = Borrowed(book = book)
    db.session.add(borrowed)
    db.session.commit()

def delete_book(book_title):
    book = Book.query.filter_by(title=book_title).first()
    borrowed = Borrowed.query.filter_by(book_id=book.id).first()
    if borrowed is not None:
        db.session.delete(borrowed)
    db.session.delete(book)
    db.session.commit()

def load():
    books_list = []
    books = Book.query.all()
    for book in books:
        temp_book = {}
        temp_book["title"] = book.title
        temp_book["author"] = book.author
        borrowed = Borrowed.query.filter_by(book_id=book.id).first()
        if borrowed is not None:
            temp_book['borrowed_date'] = borrowed.borrowed_date
        else:
            temp_book['borrowed_date'] = ""
        books_list.append(temp_book)
    return books_list

db.create_all()  # czy to jest odpowiednie miejsce?