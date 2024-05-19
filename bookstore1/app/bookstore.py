from flask import Flask
from sqlalchemy import create_engine

from infra.storage.sqlite_storage import db
from views.book import bp as book_bp
from context_ import Context_


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context_()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookstore1.db"
    db.init_app(app)
    return app


app = create_app()
