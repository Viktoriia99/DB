from app import app, db
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/home/index')
def index():
    from app import Book
    books1 = Book.query.all()
    books2 = db.session.query(Book.author, Book.title, Book.price).all()
    books3 = db.session.query(Book.author.label('Автор'), Book.title.label('Название')).all()
    books4 = db.session.query(Book.title, Book.amount, (Book.amount * 1.65).label('pack')).all()
    books5 = db.session.query(Book.author, Book.title, Book.price).filter(Book.amount < 10).all()
    books6 = db.session\
        .query(Book.title, Book.author, Book.price, Book.amount)\
        .filter((Book.price < 500) | (Book.price > 600))\
        .filter(Book.price * Book.amount >= 5000)\
        .all()
    books7 = db.session\
        .query(Book.author, Book.title)\
        .filter(Book.price.between(540.5, 800)) \
        .filter(Book.amount.in_([2, 3, 5, 7])) \
        .all()
    books8 = db.session \
        .query(Book.author, Book.title) \
        .filter(Book.title.like("_% _%")) \
        .filter(Book.author.like("% С.%")) \
        .all()
    books9 = db.session \
        .query(Book.author, Book.title) \
        .filter(Book.amount.between(2, 14)) \
        .order_by(db.desc(Book.author), Book.title) \
        .all()

    for book in Book.query.all():
        db.session.delete(book)
    db.session.commit()

    book1 = Book(book_id=1, title='Мастер и Маргарита', author='Булгаков М.А.', price=670.99, amount=3)
    book2 = Book(book_id=2, title='Белая гвардия', author='Булгаков М.А.', price=540.50, amount=5)
    book3 = Book(book_id=3, title='Идиот', author='Достоевский Ф.М.', price=460.00, amount=10)
    book4 = Book(book_id=4, title='Братья Карамазовы', author='Достоевский Ф.М.', price=799.01, amount=3)
    book5 = Book(book_id=5, title='Игрок', author='Достоевский Ф.М.', price=480.50, amount=10)
    book6 = Book(book_id=6, title='Стихотворения и поэмы', author='Есенин С.А.', price=650.00, amount=15)
    db.session.add_all([book1, book2, book3, book4, book5, book6])
    db.session.commit()

    books10 = db.session.query(Book.amount.distinct().label('amount')).all()

    return render_template(
        "home/select.html",
        books1=books1,
        books2=books2,
        books3=books3,
        books4=books4,
        books5=books5,
        books6=books6,
        books7=books7,
        books8=books8,
        books9=books9,
        books10=books10,
        )

@app.route('/about')
@app.route('/home/about')
def about():
    # ...
    return render_template(
        "home/about.html",
        )

@app.route('/contact')
@app.route('/home/contact')
def contact():
    # ...
    return render_template(
        "error/404.html",
        ), 404
