# Schema_mixin.py: Marshmallow schema mix-in
from __future__ import unicode_literals

from error import APIError

# Schema mix-in class
class SchemaMixin(object):
    # Load data
    def load_data(self, data):
        obj, error = self.load(data)
        if error:
            raise APIError(400, "ArgFormatError", errors=error)
        return obj
    # Dump data
    def dump_data(self, obj):
        data, _ = self.dump(obj)
        return data
