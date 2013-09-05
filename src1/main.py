import sys
import platform

import numpy as np
import PySide
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton, QMessageBox, QWidget, QVBoxLayout


__version__ = '0.0.1'

from testUi01 import Ui_MainWindow # testUi01 is generated from testUi01.ui using pyside-uic. Qt Designer was used to create the .ui file.  The matplot widget had to be "Promoted" in Qt Designer.
from MvcModel.MathModelController import MathModelController
from PhGui.MainGuiController import MainGuiController

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.main_frame = Ui_MainWindow()
        self.main_frame.setupUi(self)

        self.valueChanged = QtCore.Signal(int)

        
    def simulateButtonPushed(self):
        self.mainGuiController.simulateButtonPushed();

    def co2sinkValueChanged(self, value):
      self.mainGuiController.co2sinkValueChanged(value)

    def plot1(self, voiHistory, statesHistory, algebraicsHistory):
        self.main_frame.widget.axes.plot(voiHistory, np.vstack((statesHistory,algebraicsHistory)).T)
        self.main_frame.widget.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    frame = MainWindow()
    frame.main_frame.pushButton.clicked.connect(frame.simulateButtonPushed)

    frame.mainGuiController = MainGuiController(frame)
    
    frame.main_frame.co2sink.valueChanged.connect(frame.co2sinkValueChanged)
    

    frame.show()
    app.exec_()
    
