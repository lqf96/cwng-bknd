# Metadata.py: Object metadata
from __future__ import unicode_literals

# Add metadata
def add_metadata(obj, name, value):
    metadata = getattr(obj, "__cw_metadata__", {})
    metadata[name] = value
    obj.__cw_metadata__ = metadata

# Has metadata
def has_metadata(obj, name):
    return hasattr(obj, "__cw_metadata__") and name in obj.__cw_metadata__

# Get metadata
def get_metadata(obj, name, default=None):
    return obj.__cw_metadata__[name] if has_metadata(obj, name) else default
