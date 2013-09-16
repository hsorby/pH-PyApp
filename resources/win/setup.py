
from distutils.core import setup
import py2exe
import matplotlib

APP = [{'script': 'src/main.py'}]
DATA_FILES = matplotlib.get_py2exe_datafiles()
OPTIONS = {}

setup(
	windows=APP,
	options=OPTIONS,
	data_files=DATA_FILES
)