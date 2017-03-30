
# Copyright (C) 2014-2015, Availab.io(R) Ltd. All rights reserved.
from street_book.app import app, api
from street_book.config import Config

from street_book.resources.book_page import BookPage
from street_book.resources.book_page_code import BookPageCode
from street_book.resources.codes import Codes

api.add_resource(BookPage, "/books/<string:book_name>/pages/<string:page_id>")
api.add_resource(BookPageCode, "/books/<string:book_name>/pages/<string:page_id>/qr")
api.add_resource(Codes, "/books/<string:book_name>/qr")

app.config.from_object(Config)
