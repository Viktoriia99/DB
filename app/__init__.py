from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import home_controller
from app.controllers import support_controller
from app import routes, errors
from app.models.book import Book


if not Book.query.first():
    book1 = Book(book_id=1, title='Мастер и Маргарита', author='Булгаков М.А.', price=670.99, amount=3)
    book2 = Book(book_id=2, title='Белая гвардия', author='Булгаков М.А.', price=540.50, amount=5)
    book3 = Book(book_id=3, title='Идиот', author='Достоевский Ф.М.', price=460.00, amount=10)
    book4 = Book(book_id=4, title='Братья Карамазовы', author='Достоевский Ф.М.', price=799.01, amount=2)
    book5 = Book(book_id=5, title='Стихотворения и поэмы', author='Есенин С.А.', price=650.00, amount=15)
    db.session.add_all([book1, book2, book3, book4, book5])
    db.session.commit()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book}
