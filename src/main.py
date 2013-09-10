import sys
import platform

import numpy as np
import PySide
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton, QMessageBox, QWidget, QVBoxLayout


__version__ = '0.0.1'

from mainui import Ui_MainWindow # mainui is generated from mainui.ui using pyside-uic. Qt Designer was used to create the .ui file.  The matplot widget had to be "Promoted" in Qt Designer.
from mvcmodel.mathmodelcontroller import MathModelController
from phgui.mainguicontroller import MainGuiController

speed=300 # todo: this needs to be able to be adjusted from UI.


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.main_frame = Ui_MainWindow()
        self.main_frame.setupUi(self)
        
        self.valueChanged = QtCore.Signal(int)

        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.update)
        timer.start(speed)

  
    def update(self):
          self.mainGuiController.timerEvent()


    def plot1(self, voiHistory, statesHistory, algebraicsHistory):
        self.main_frame.plotArea.axes.plot(voiHistory, np.vstack((statesHistory,algebraicsHistory)).T)
        self.main_frame.plotArea.draw()
        
    def reset(self, co2SinkValue, co2SourceValue, protonSourceValue):
      self.main_frame.plotArea.axes.clear()
      self.main_frame.plotArea.draw()
      
      self.main_frame.co2Sink.setValue(co2SinkValue)
      self.main_frame.co2Source.setValue(co2SourceValue)
      self.main_frame.protonSource.setValue(protonSourceValue)
      
    def setCo2SourceValue(self, value):
      self.main_frame.co2SourceValue.setText(str(value))
      
    def setCo2SinkValue(self, value):
      self.main_frame.co2SinkValue.setText(str(value))
      
    def setProtonSourceValue(self, value):
      self.main_frame.protonSourceValue.setText(str(value))
      
    def playPauseLabelToggle(self, running):
      if (running):
        text = "Pause"
      else:
        text = "Run"
      self.main_frame.simulateButton.setText(text)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    frame = MainWindow()

    frame.mainGuiController = MainGuiController(frame)

    frame.main_frame.simulateButton.clicked.connect(frame.mainGuiController.playPauseButtonPushed)
    frame.main_frame.resetButton.clicked.connect(frame.mainGuiController.resetButtonPushed)

    frame.main_frame.co2Source.valueChanged.connect(frame.mainGuiController.co2SourceValueChanged)
    frame.main_frame.co2Sink.valueChanged.connect(frame.mainGuiController.co2SinkValueChanged)
    frame.main_frame.protonSource.valueChanged.connect(frame.mainGuiController.protonSourceValueChanged)
    

    frame.show()
    app.exec_()
    
