
from distutils.core import setup
import py2exe

APP = [{'script': 'src/main.py'}]
DATA_FILES = []
OPTIONS = {}

setup(
	windows=APP,
	options=OPTIONS,
)