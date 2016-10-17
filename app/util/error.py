# Errors.py: Website error classes
from __future__ import unicode_literals

from flask import jsonify
from app import app

# API error
class APIError(Exception):
    # Constructor
    def __init__(self, status, type, **kwargs):
        super(APIError, self).__init__(dict(status="failed", type=type, **kwargs))
        self.status = status

# API error handler
@app.errorhandler(APIError)
def api_error_handler(e):
    return jsonify(e.message), e.status

# SQLAlchemy error handlers
