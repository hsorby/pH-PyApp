import phcontrol
from numpy import *

class MathModelState(object):
  """
  Keeps overall state for pH model, which allows a series of solves, each picking up where the previous left off.
  """
  
  def __init__(self):
    self.reset()


  def reset(self):
    """
    Reset variable of integration (voi) (voi is time in this model)
    """
    
    self.voiStart = 0
    self.voiRange = 10
    self.voiStepCount = 500
    (self.init_states, self.constants) = phcontrol.initConsts()

    self.algebraicsHistory = atleast_2d([])
    self.statesHistory = atleast_2d([])
    self.voiHistory = []


  def solve(self):
    """
    Solve using values for state variables from this object instance's member for them.  Append solution to historic solution.
    """

    voi = linspace(self.voiStart, self.voiStart + self.voiRange, self.voiStepCount)
    (voi, states1, algebraics1) = phcontrol.solve_model(self.init_states, self.constants, voi)

    self.voiStart = voi[len(voi)-1]
    self.init_states = states1[:,len(states1)-1]

    self.statesHistory = append(self.statesHistory, states1, axis=0)
    self.algebraicsHistory = append(self.algebraicsHistory, algebraics1, axis=0)
    self.voiHistory = append(self.voiHistory, voi, axis=0)

