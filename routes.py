from flask import render_template, request, redirect
from extensions import db
from models import Book, BookCategory


def init_routes(app):
    @app.route('/')
    def get_base():
        return render_template('base.html')

    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            description = request.form['description']
            publisher = request.form['publisher']
            pages = request.form['pages']
            category = request.form['category']

            book = Book(
                title=title,
                author=author,
                description=description,
                publisher=publisher,
                pages=pages,
                category=category)

            db.session.add(book)
            db.session.commit()
            return redirect('/')

        categories = BookCategory.query.all()
        return render_template('add_book.html', categories=categories)

    @app.route('/book_list')
    def get_book_list():
        books = Book.query.all()
        return render_template('book_list.html', books=books)
