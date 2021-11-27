from app import db


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    price = db.Column(db.Numeric(8, 2))
    amount = db.Column(db.Integer)

    def __repr__(self):
        return f'<Book {self.book_id}\t{self.title}\t{self.author}\t{self.price}\t{self.amount}>'
