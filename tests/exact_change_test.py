import unittest

from exact_change import isValidDollarAmount, CalcDenominationQuantity, CalculateExactChange

class TestExactChange(unittest.TestCase):

  # isValidDollarAmount
  # true
  # false
  def test_whenDollarAmountIs100_thenIsValidDollarAmountTrue(self):
    self.assertTrue(isValidDollarAmount(100))

  def test_whenDollarAmountIsPoint2_thenIsValidDollarAmountTrue(self):
    self.assertTrue(isValidDollarAmount(0.2))

  def test_whenDollarAmountIs0_thenIsValidDollarAmountTrue(self):
    self.assertTrue(isValidDollarAmount(0))

  def test_whenDollarAmountIsNegative1_thenIsValidDollarAmountFalse(self):
    self.assertFalse(isValidDollarAmount(-1))

  def test_whenDollarAmountIsNegativePoint2_thenIsValidDollarAmountFalse(self):
    self.assertFalse(isValidDollarAmount(-0.2))


  # CalcDenominationQuantity
  # dollarAmount 0
  #   Hundred


if __name__ == '__main__':
  unittest.main()

  
  
