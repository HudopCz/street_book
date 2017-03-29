# Copyright (C) 2015, Availab.io(R) Ltd. All rights reserved.
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
