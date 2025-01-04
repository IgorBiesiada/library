from extensions import db

class BookCategory(db.Model):
    __tablename__ = 'book_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __str__(self):
        return self.name

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('book_category.id'), nullable=False)
    category = db.relationship('BookCategory', backref=db.backref('books', lazy=True))

    def __str__(self):
        return f'{self.title} - {self.author}'