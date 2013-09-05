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


    def plot1(self, voiHistory, statesHistory, algebraicsHistory):
        self.main_frame.plotArea.axes.plot(voiHistory, np.vstack((statesHistory,algebraicsHistory)).T)
        self.main_frame.plotArea.draw()
        
    def reset(self, co2SinkValue, co2SourceValue, protonSourceValue):
      self.main_frame.plotArea.axes.clear()
      self.main_frame.plotArea.draw()
      
      self.main_frame.co2Sink.setValue(co2SinkValue)
      self.main_frame.co2Source.setValue(co2SourceValue)
      self.main_frame.protonSource.setValue(protonSourceValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    frame = MainWindow()

    frame.mainGuiController = MainGuiController(frame)

    frame.main_frame.simulateButton.clicked.connect(frame.mainGuiController.simulateButtonPushed)
    frame.main_frame.resetButton.clicked.connect(frame.mainGuiController.resetButtonPushed)

    frame.main_frame.co2Source.valueChanged.connect(frame.mainGuiController.co2SourceValueChanged)
    frame.main_frame.co2Sink.valueChanged.connect(frame.mainGuiController.co2SinkValueChanged)
    frame.main_frame.protonSource.valueChanged.connect(frame.mainGuiController.protonSourceValueChanged)
    

    frame.show()
    app.exec_()
    
