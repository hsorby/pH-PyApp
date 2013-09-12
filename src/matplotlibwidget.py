# This code and technique is from http://stackoverflow.com/questions/9500661/connecting-pyside-with-matplotlib-using-qtdesigner-using-pushbutton-to-draw
# Add a widget in Qt Designer, then promote it to MatplotlibWidget, ignore the fact that the file name field suffixes a .h extension.
#
import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'


from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas



class MatplotlibWidget(FigureCanvas):

    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(Figure())
        
        self.setParent(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        
