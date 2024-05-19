import dataclasses
import json

from flask import Blueprint, current_app, request, make_response, jsonify

from context_ import get_context
from domain.book import Book
from marshmallow import ValidationError

from views.book_shema import Book_Schema

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)
    books = ctx.book_service.get_all()
    response = make_response(Book_Schema(many=True).dump(books))
    response.headers['Content-Type'] = 'application/json'

    return response, 200


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)
    try:
        book_data = Book_Schema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    book = Book(**book_data)
    try:
        book = ctx.book_service.add(book)
    except Exception as e:
        return {
            "errorrrr": "failed to add book",
            "data": book_data
        }
    response = make_response(Book_Schema().dump(book))
    response.headers['Content-Type'] = 'application/json'
    return response, 201


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)
    response = make_response({"status": f"book with id {id} successfully deleted"})
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/<id>")
def get_book_by_id(id):
    ctx = get_context(current_app)

    book = ctx.book_service.get_book_by_id(id)

    if book:

        response = make_response(Book_Schema().dump(book))
        response.headers['Content-Type'] = 'application/json'
        return response,
    if book is None:
        response1 = make_response({
            "error": 'Not found'
        }, )
        response1.headers['Content-Type'] = 'application/json'
        return response1, 404
