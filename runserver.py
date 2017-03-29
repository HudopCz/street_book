#!env/bin/python
# Copyright (C) 2015, Availab.io(R) Ltd. All rights reserved.
import sys
from street_book.app import app
import street_book.startup

if __name__ == '__main__':
    app.run()
