#! /usr/bin/env python2.7
import os
from app import app

# Change working directory
os.chdir(os.path.dirname(__file__))
# Run application
app.run(debug=True)
