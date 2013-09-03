import sys
import platform

import numpy as np
import PySide
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton, QMessageBox, QWidget, QVBoxLayout

import MvcModel.MathModelState

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


__version__ = '0.0.1'

from testUi01 import Ui_MainWindow # testUi01 is generated from testUi01.ui using pyside-uic. Qt Designer was used to create the .ui file.  The matplot widget had to be "Promoted" in Qt Designer.
from MvcModel.MathModelState import MathModelState

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.main_frame = Ui_MainWindow()
        self.main_frame.setupUi(self)

        self.mathModelState = MathModelState()
        
#         self.simCount = 0

    def plot_stuff(self):

        self.mathModelState.solve()

#         self.simCount += 1
#         
#         np.savetxt("voi" + `self.simCount` + ".csv", self.mathModelState.voiHistory, delimiter=",")
#         np.savetxt("states" + `self.simCount` + ".csv", self.mathModelState.statesHistory, delimiter=",")
#         np.savetxt("algebraic" + `self.simCount` + ".csv", self.mathModelState.algebraicsHistory, delimiter=",")


        self.main_frame.widget.axes.plot(self.mathModelState.voiHistory, np.vstack((self.mathModelState.statesHistory,self.mathModelState.algebraicsHistory)).T)
        self.main_frame.widget.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()

    frame.main_frame.pushButton.clicked.connect(frame.plot_stuff)

    frame.show()
    app.exec_()
    
