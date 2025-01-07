import os

from flask import render_template, request
from extensions import db
from models import Book, BookCategory
from config import Config
from werkzeug.utils import secure_filename


def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

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


            if 'image_path' in request.files:
                image = request.files['image_path']
                if image and allowed_file(image.filename):
                    filename = secure_filename(image.filename)
                    image_path = os.path.join(Config.UPLOAD_FOLDER, filename)
                    image.save(image_path)
                else:
                    image_path = None
            else:
                image_path = None

            book = Book(
                title=title,
                author=author,
                description=description,
                publisher=publisher,
                pages=pages,
                category_id=category_id,
                image_path=image_path
            )

            db.session.add(book)
            db.session.commit()


        return render_template('add_book.html', categories=categories)

    @app.route('/book_list')
    def get_book_list():
        books = Book.query.all()
        return render_template('book_list.html', books=books)
