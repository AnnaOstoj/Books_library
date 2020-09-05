from flask import request, render_template, redirect, url_for
from app import app, db
from app import models
from forms import BookForm


@app.route("/library/books", methods=["GET", "POST"])
def show_library():
    error=""
    book_form = BookForm()

    if request.method == "POST":
        if book_form.validate_on_submit(): 
            models.add_book(book_form)
            return redirect(url_for('show_library'))
            
    books_list = models.load()
    return render_template("homepage.html", form = book_form, books = books_list, error=error)


@app.route("/library/borrow", methods=["GET", "POST"])
def borrow_book():
    if request.method == "POST":
        book_title = request.args.get('book_title')
        models.borrow_book(book_title)
    return redirect(url_for('show_library'))


@app.route("/library/delete", methods=["GET", "POST"])
def delete_book():
    if request.method == "POST":
        book_title = request.args.get('book_title')
        models.delete_book(book_title)
    return redirect(url_for('show_library'))