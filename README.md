pH-PyApp
========
Educational application for demonstrating human pH homeostasis

Code by Randall Britten, Auckland Bioengineering Institute, University of Auckland

Other team members:
* Peter Hunter, Auckland Bioengineering Institute, University of Auckland
* Bernard de Bono

August 2013

Development environment setup
=============================
* Install Python
* Install SciPy and Numpy (from Christoph Gohlke if on windows http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy, http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
* Install Qt (at time of writing, v4.8.5 is compatible with PySide 1.2.1) 
* Install PySide
* Install Eclipse (requires installation of Java JVM)
* Install Pydev (Installed through eclipses 'Help/Install new software' menu option)
* Install Git (might already be available via Eclipse, depending on your version of Eclipse)

Notes
=====
* Edit .ui files using Qt Designer
* Use pyside-uic to generate .py from .ui
* Main program is main.py
* phcontrol.py is mostly just the code generated from the CellML file at http://models.cellml.org/workspace/178
* To generate code, get the CellML-API (http://cellml-api.sourceforge.net), and run testCeLEDS using python.xml (under CeLEDS languages folder in CellML-API source)
* Tested on Windows 7 64 bit and GNU/Linux 64 bit platforms.  Should also work on OSX.

Todo
====
* Continuous simulation interactive "real-time" mode, where adjusting sliders updates parameters as simulation runs.
* Current code is still a bit of a copy-n-paste-n-hack shambles to check that all the pieces will work together, and because a lot of the tools were being learned, it still needs design at the code level.
  Some progress here: small clean ups being done at each commit.
* Automated tests
* Figure out how to create Installer and then create scripts to make Installer
* Disable sliders that adjust model parameters during a solve.  This does not mean that it can't be made "real-time interactive", to do that, solves will just be done in short bursts.
* Display parameter values, currently one has to guess their values from the slider positions.
* Display Legend for plots
* Allow user to select colour and line style
* Pan and zoom plot
* Units for plot axes
* Show other variables on plot, especially parameters that are under user control
* Consider using a separate thread for solve.
* Internationalisation, rather than hard-coded message and lable strings.

