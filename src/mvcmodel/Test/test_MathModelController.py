import unittest
import mvcmodel.mathmodelcontroller

class Test_MathModelController(unittest.TestCase):
  def test_reset(self):
    m = mvcmodel.mathmodelcontroller.MathModelController()
    
    self.assertEqual(m.statesHistory.size, 0, "Pristine MathModelController should have blank history: states")
    self.assertEqual(m.algebraicsHistory.size, 0, "Pristine MathModelController should have blank history: algebraics")
    self.assertEqual(m.voiHistory.size, 0, "Pristine MathModelController should have blank history: voi")
    self.assertEqual(m.voiStart, 0, "Pristine MathModelController should have voiStart set to 0")
    voiRange = m.voiRange
    
    m.solve()
    
    
    statesLength01 = m.statesHistory.size
    self.assertGreater(statesLength01, 0, "After solve, MathModelController should have some history: states")
    algebraicsLength01 = m.algebraicsHistory.size
    self.assertGreater(algebraicsLength01, 0, "After solve, MathModelController should have some history: algebraics")
    voiLength01 = m.voiHistory.size
    self.assertGreater(voiLength01, 0, "After solve, MathModelController should have some history: voi")
    self.assertEqual(m.voiStart, voiRange, "After first solve, voiStart (for next solve) should equal voiRange")

    m.solve()

    self.assertEqual(m.statesHistory.size, 2 * statesLength01, "After 2nd solve, MathModelController should have twice as much history: states")
    self.assertEqual(m.algebraicsHistory.size, 2 * algebraicsLength01, "After 2nd solve, MathModelController should have twice as much history: algebraics")
    self.assertEqual(m.voiHistory.size, 2 * voiLength01, "After 2nd solve, MathModelController should have twice as much history: voi")

    self.assertEqual(m.voiStart, 2 * voiRange, "After second solve, voiStart (for next solve) should have increased again by voiRange")
    
    
    m.reset()
    
    self.assertEqual(m.statesHistory.size, 0, "After reset MathModelController should have blank history: states")
    self.assertEqual(m.algebraicsHistory.size, 0, "After reset MathModelController should have blank history: algebraics")
    self.assertEqual(m.voiHistory.size, 0, "After reset MathModelController should have blank history: voi")
