from flask import render_template, request, redirect
from extensions import db
from models import Book, BookCategory


def init_routes(app):
    @app.route('/')
    def get_base():
        return render_template('base.html')

    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        categories = BookCategory.query.all()

        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            description = request.form['description']
            publisher = request.form['publisher']
            pages = request.form['pages']
            category_id = request.form['category']
            image = request.form['image']

            book = Book(
                title=title,
                author=author,
                description=description,
                publisher=publisher,
                pages=pages,
                category_id=category_id,
                image=image
            )

            db.session.add(book)
            db.session.commit()


        return render_template('add_book.html', categories=categories)

    @app.route('/book_list')
    def get_book_list():
        books = Book.query.all()
        return render_template('book_list.html', books=books)
