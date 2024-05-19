from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class SqliteStorage:
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_book_by_id(self, id):
        from domain.book import Book
        book = Book.query.get(id)

        return book

    def get_all(self):
        try:
            from domain.book import Book
            books = Book.query.all()
            return books

        except NoResultFound as NoRes:
            sub_report_id = []
            return sub_report_id

    def add(self, book):
        db.session.add(book)
        db.session.commit()
        return book

    def delete(self, id):
        from domain.book import Book
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return book
