pH-PyApp
========
Educational app for demonstrating human pH homeostasis
By Randall Britten, Auckland Bioengineering Institute, University of Auckland
August 2013

Development environment setup
=============================
* Install Python and SciPy (on Windows, this is bundled for example in the Anaconda installer)
* Install Qt (at time of writing, v4.8.5 is compatible with PySide 1.2.1) 
* Install PySide
* Install Eclipse (requires installation of Java JVM)
* Install Pydev
* Install Git (might already be available via Eclipse, depending on your version of Eclipse)

Notes
=====
* Edit .ui files using Qt Designer
* Use pyside-uic to generate .py from .uic
* Main program is main.py
* phcontrol.py is mostly just the code generated from the CellML file at http://models.cellml.org/workspace/178
* To generate code, get the CellML-API (http://cellml-api.sourceforge.net), and run testCeLEDS using python.xml (under CeLEDS languages folder in CellML-API source)
* Only tested on Windows 7 64 bit platform so far.

Todo
====
* Actually create something useful in the UI.
* Current code is just a copy-n-paste-n-hack shambles to check that all the pieces will work together, and because a lot of the tools are being learned, it design at the code level.
* Automated tests
* Figure out how to create Installer and then create scripts to make Installer



