#!env/bin/python
import sys
import os

parentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,parentdir)
activate_env=os.path.expanduser(parentdir + "/env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import street_book.startup
from street_book.app import app as application
