# User.py: User related operations
from __future__ import unicode_literals

from hashlib import pbkdf2_hmac
from flask import session
from app.config import USER_PASSWD_HMAC_SALT, N_HASH_ROUNDS

# Authenticate user
def authenticate(username, password):
    hashed_password = pbkdf2_hmac("sha256", raw_password, USER_PASSWD_HMAC_SALT, N_HASH_ROUNDS)
    return User.query.filter_by(username=username, password=hashed_password).first()

# Log user in
def login(user):
    session["user"] = user

# Log user out
def logout():
    session["user"] = None
