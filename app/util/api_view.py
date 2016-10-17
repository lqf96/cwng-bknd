# Api_view.py: Pluggable API view
from __future__ import unicode_literals

from flask.views import MethodView
from app import app
from metadata import add_metadata, has_metadata, get_metadata

# API view class
class APIView(MethodView):
    # Action handlers
    _api_action_handlers = {}
    _res_action_handlers = {}
    # GET
    def get(self, id):
        if id==None:
            return self.list()
        else:
            return self.retrieve(id)
    # POST
    def post(self, action):
        # Create resource
        if action==None:
            return self.create()
        # API action
        else:
            cls = self.__class__
            handler = cls.__api_action_handlers.get(action)
            if handler:
                return handler(self)
    # PATCH
    def patch(self, id):
        return self.update(id)

# Register API action
def api_action(name, method=None):
    # Decorator style
    if method==None:
        return lambda method: api_action(name, method)
    # Add API action metadata
    add_metadata(method, u"api_action", name)
    return method

# Register routes
def route(endpoint, url, view=None):
    # Decorator style
    if view==None:
        return lambda view: route(endpoint, url, view)
    #
    for member in view.__dict__.values():
        # API action
        if has_metadata(member, "api_action"):
            action = get_metadata(member, "api_action")
            view._api_action_handlers[action] = member
    # Register routes
    view_func = view.as_view(endpoint.encode("utf-8"))
    app.add_url_rule(url, defaults={"id": None}, view_func=view_func, methods=["GET"])
    app.add_url_rule(url, defaults={"action": None}, view_func=view_func, methods=["POST"])
    app.add_url_rule("%s/<string:action>" % url, view_func=view_func, methods=["POST"])
    app.add_url_rule("%s/<int:id>" % url, view_func=view_func, methods=["GET", "PATCH", "DELETE"])
    # Return view
    return view
