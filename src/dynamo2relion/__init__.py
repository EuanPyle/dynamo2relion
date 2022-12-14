"""Converts Dynamo tables to RELION particle star files."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dynamo2relion")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Euan Pyle"
__email__ = "euanpyle@gmail.com"