from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from infra.storage.sqlite_storage import db


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    author: Mapped[str] = mapped_column(String)
    publish_year: Mapped[int] = mapped_column(Integer)
    pages_count: Mapped[int] = mapped_column(Integer)
