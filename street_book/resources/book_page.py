import jinja2
import json
from flask_restful import Resource
from flask import make_response

from street_book.app import app
from street_book.books import books

class BookPage(Resource):
    """
    Return content of one page if correct id is provided

    This is the main resource of the application.
    """

    def get(self, book_name, page_id):
        """
        Return content for specific page of the book
        """
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                './street_book/templates'
            )
        )

        if not books.get(book_name) or not books[book_name].get(page_id):
            tmpl = env.get_template("404.html")
            return make_response(tmpl.render({}), 404)
        else:
            tmpl = env.get_template("page.html")
            return make_response(tmpl.render(
                {
                    "book_name": book_name,
                    "base_url": app.config["BASE_URL"],
                    "text": books[book_name][page_id]["text"]
                }
            ))
