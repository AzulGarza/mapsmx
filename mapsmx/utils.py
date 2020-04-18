import os
import sys
import importlib

def get_file_name(package, resource):

    #taken from
    #  https://github.com/python/cpython/blob/master/Lib/pkgutil.py
    spec = importlib.util.find_spec(package)
    if spec is None:
        return None
    loader = spec.loader
    if loader is None or not hasattr(loader, 'get_data'):
        return None
    # XXX needs test
    mod = (sys.modules.get(package) or
           importlib._bootstrap._load(spec))
    if mod is None or not hasattr(mod, '__file__'):
        return None

    # Modify the resource name to be compatible with the loader.get_data
    # signature - an os.path format "filename" starting with the dirname of
    # the package's __file__
    parts = resource.split('/')
    parts.insert(0, os.path.dirname(mod.__file__))
    resource_name = os.path.join(*parts)

    return resource_name
