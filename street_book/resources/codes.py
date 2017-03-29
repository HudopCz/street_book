import jinja2
import json
import base64
import qrcode
import cStringIO

from flask_restful import Resource
from flask import make_response

from street_book.app import app
from street_book.books import books

class Codes(Resource):
    """
    Return content of one page if correct id is provided

    This is the main resource of the application.
    """

    def get(self, book_name):
        """
        Return content for specific page of the book
        """
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                './street_book/templates'
            )
        )

        if not books.get(book_name):
            tmpl = env.get_template("404.html")
            return make_response(tmpl.render({}), 404)
        else:
            items = []
            for page_id, value in books[book_name].iteritems():

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                url = '{0}/books/{1}/pages/{2}'.format(
                    app.config["BASE_URL"], book_name, page_id
                )
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image()

                buffer = cStringIO.StringIO()
                img.save(buffer, format="PNG")

                items.append({
                    "url": url,
                    "img": "data:image/png;base64, " + base64.b64encode(
                        buffer.getvalue()
                    )
                })

            tmpl = env.get_template("qr_codes.html")
            return make_response(tmpl.render(
                {
                    "codes": items
                }
            ))
