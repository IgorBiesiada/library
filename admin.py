from models import BookCategory
from extensions import db
from app import create_app

app = create_app()

def add_book_category(name):
    with app.app_context():
        category = BookCategory(name=name)
        db.session.add(category)
        db.session.commit()

if __name__ == '__main__':
     add_book_category('Horror')