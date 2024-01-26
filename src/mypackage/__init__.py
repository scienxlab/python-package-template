from .mypackage import *
from .cli import cli

# It used to be conventional to define a __version__ attribute.
# However, it is now considered best practice to get version
# information from the package metadata directly, eg by using
# importlib.metadata.version (see below).
#
# If you still want to define __version__, uncomment the following:
#
# from importlib.metadata import version
# __version__ = version(__package__ or __name__)
