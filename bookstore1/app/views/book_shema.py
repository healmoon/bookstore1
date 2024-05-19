from marshmallow import Schema, fields


class Book_Schema(Schema):
    id = fields.Integer()
    title = fields.String()
    author = fields.String()
    publish_year = fields.Integer()
    pages_count = fields.Integer()
