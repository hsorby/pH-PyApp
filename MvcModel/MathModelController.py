import phcontrol
from numpy import *

class MathModelController(object):
  """
  Keeps overall state for pH model, which allows a series of solves, each picking up where the previous left off.
  """
  
  def __init__(self):
    self.reset()
    (legend_states, legend_algebraic, legend_voi, legend_constants) = phcontrol.createLegends()
    self.co2SinkIndex = legend_constants.index("CO2sink in component Flux (mM_per_second)")
    self.co2SourceIndex = legend_constants.index("CO2source in component Flux (mM_per_second)")
    self.protonSourceIndex = legend_constants.index("protonSource in component Flux (mM_per_second)")


  def reset(self):
    """
    Reset variable of integration (voi) (voi is time in this model)
    """
    
    self.voiStart = 0
    self.voiRange = 10 # todo: This needs to be able to be set from UI, but depends on whether UI has "real time" simulation.
    self.voiStepCount = 500 # todo: This should be set from UI, say under "settings".
    (self.init_states, self.constants) = phcontrol.initConsts()

    self.algebraicsHistory = []
    self.statesHistory = []
    self.voiHistory = []


  def solve(self):
    """
    Solve using values for state variables from this object instance's member for them.  Append solution to historic solution.
    """

    voi = linspace(self.voiStart, self.voiStart + self.voiRange, self.voiStepCount)
    (voi, states1, algebraics1) = phcontrol.solve_model(self.init_states, self.constants, voi)

    self.voiStart = voi[len(voi)-1]

    if (len(self.voiHistory) < 1) :
      self.statesHistory = states1
      self.algebraicsHistory = algebraics1
      self.voiHistory = voi
    else:
      self.statesHistory = hstack((self.statesHistory, states1))
      self.algebraicsHistory = hstack((self.algebraicsHistory, algebraics1))
      self.voiHistory = hstack((self.voiHistory, voi))

    historyCount = len(self.voiHistory)
    self.init_states = self.statesHistory[:,historyCount-1]

    
  def setCo2SinkValue(self, value):
    self.co2SinkValue = value
    self.constants[self.co2SinkIndex] = value

    
  def setCo2SourceValue(self, value):
    self.co2SourceValue = value
    self.constants[self.co2SourceIndex] = value


  def setProtonSourceValue(self, value):
    self.protonSourceValue = value
    self.constants[self.protonSourceIndex] = value

