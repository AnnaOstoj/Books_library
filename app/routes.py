from flask import request, render_template, redirect, url_for
from app import app, db
from app import models
from forms import BookForm


@app.route("/library/", methods=["GET", "POST"])
def show_library():
    error=""
    book_form = BookForm()
    books_list = models.load()
    #gdy robię add book, to lista się nie updatuje. Dane pojawiają się w formularzu. Update dzieje się w bazie
    #jak przekazać book_title, żeby zmienna nie wyświetliła się w url?
    if request.method == "POST":
        if book_form.validate_on_submit(): 
            if request.form["btn"] == "Add Book":
                models.add_book(book_form)
                redirect(url_for('show_library'))

        if request.form["btn"] == "Borrow":
            book_title = request.args.get('book_title')
            models.borrow_book(book_title)
            redirect(url_for('show_library'))

        if request.form["btn"] == "Delete":
            book_title = request.args.get('book_title')
            models.delete_book(book_title)
            redirect(url_for('show_library', book_title =""))


    return render_template("homepage.html", form = book_form, books = books_list, error=error)