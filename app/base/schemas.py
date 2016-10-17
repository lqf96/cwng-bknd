# Schemas.py: Website basic schemas
from __future__ import unicode_literals

from hashlib import pbkdf2_hmac
from marshmallow import Schema, fields, validate, post_load
from app.config import USER_PASSWD_HMAC_SALT, N_HASH_ROUNDS
from app.util.schema_mixin import SchemaMixin
from app.base.models import User

# User schema
class UserSchema(Schema, SchemaMixin):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(4, 32))
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.Method("calc_password", required=True, load_only=True)
    join_date = fields.DateTime(dump_only=True)
    active = fields.Boolean(dump_only=True)
    # Calculate password
    def calc_password(self, raw_password):
        return pbkdf2_hmac("sha256", raw_password, USER_PASSWD_HMAC_SALT, N_HASH_ROUNDS)
    # Post load hook
    @post_load
    def make_user(self, data):
        return User(**data)
