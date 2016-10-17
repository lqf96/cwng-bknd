# Views.py: RESTful API views
from __future__ import unicode_literals

from flask import request, jsonify
from app import db
from app.util import route, APIView, SUCCESS_RESP, api_action, APIError
from app.base.models import User
from schemas import UserSchema
from user import authenticate, login, logout

@route("user_view", "/users")
class UserView(APIView):
    # Create
    def create(self):
        schema = UserSchema()
        # Load user data
        user = schema.load_data(request.form)
        # Add to database
        db.session.add(user)
        db.session.commit()
        # Return success
        return jsonify(schema.dump_data(user))
    # Get user information
    def retrieve(self, id):
        schema = UserSchema()
        # Find user
        user = User.query.get(id)
        # Return failed
        return jsonify(schema.dump_data(user))
    # Update user information
    def update(self, id):
        schema = UserSchema()
        # Load update data, then find and update user
        update_data = schema.load_data(request.form)
        user = User.query.get(id)
        user.update_fields(update_data)
        db.session.commit()
        # Return success
        return jsonify(schema.dump_data(user))
    # Remove user
    def delete(self, id):
        # Find and remove user
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        # Success
        return jsonify(SUCCESS_RESP)
    # Log-in
    @api_action("login")
    def login(self):
        user = authenticate(request.form.get("username"), request.form.get("password"))
        if user:
            login(user)
            return SUCCESS_RESP
        else:
            raise APIError(401, "AuthError")
    # Log-out
    @api_action("logout")
    def logout(self):
        logout()
