# Copyright (C) 2015, Availab.io(R) Ltd. All rights reserved.
"""
Flask application and resource registration
"""
import os
import re
import json

from flask import Flask
from flask_restful import Api

from street_book.resources.book_page import BookPage

app = Flask(__name__)
api = Api(app)

api.add_resource(BookPage, "/books/<string:book_name>/pages/<string:page_id>")
