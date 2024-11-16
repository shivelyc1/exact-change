import unittest

from exact_change import isValidDollarAmount, CalcDenominationQuantity, CalculateExactChange
from Enum.denomination_values import DenominationValues
from return_types.denominations_type import DenominationsType
from exceptions.invalid_dollar_amount_range import InvalidDollarAmountRange

class TestExactChange(unittest.TestCase):
  # isValidDollarAmount()
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

  # CalcDenominationQuantity() Tests
  # Dollar amount zero
  def test_whenCalcDenominationQuantityDollarAmount0DenominationValueHUNDRED_thenReturnIs0(self):
    self.assertEqual(CalcDenominationQuantity(0, DenominationValues.HUNDRED), 0)

  # Dollar Amount = 100, DenominationValue = HUNDRED
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueHUNDRED_thenReturnIs1(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.HUNDRED), 1)

  # Dollar Amount = 100, DenominationValue = FIFTY
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueFIFTY_thenReturnIs2(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.FIFTY), 2)

  # Dollar Amount = 100, DenominationValue = TWENTY
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueTWENTY_thenReturnIs5(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.TWENTY), 5)

  # Dollar Amount = 100, DenominationValue = TEN
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueTEN_thenReturnIs10(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.TEN), 10)

  # Dollar Amount = 100, DenominationValue = FIVE
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueFIVE_thenReturnIs20(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.FIVE), 20)

  # Dollar Amount = 100, DenominationValue = ONE
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueONE_thenReturnIs100(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.ONE), 100)

  # Dollar Amount = 100, DenominationValue = QUARTER
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueQUARTER_thenReturnIs400(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.QUARTER), 400)

  # Dollar Amount = 100, DenominationValue = DIME
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueDIME_thenReturnIs1000(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.DIME), 1000)

  # Dollar Amount = 100, DenominationValue = NICKEL
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValueNICKEL_thenReturnIs2000(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.NICKEL), 2000)

  # Dollar Amount = 100, DenominationValue = PENNY
  def test_whenCalcDenominationQuantityDollarAmount100DenominationValuePENNY_thenReturnIs10000(self):
    self.assertEqual(CalcDenominationQuantity(100, DenominationValues.PENNY), 10000)


  # CalculateExactChange() Tests
  # Dollar Amount = 0 then Dictionary with denomination values are all zero
  def test_whenCalculateExactChangeDollarAmount0_thenReturnDenominationTypeIsZeros(self):
    denominationReturn: DenominationsType = {
      'hundreds': 0,
      'fifities': 0,
      'twenties': 0,
      'tens': 0,
      'fives': 0,
      'ones': 0,
      'quarters': 0,
      'dimes': 0,
      'nickels': 0,
      'pennies': 0
    }

    self.assertDictEqual(CalculateExactChange(0), denominationReturn)

  # DollarAmount = 10.003 then the Dictionary with denomination values has tens = 1 and penny = 1
  # Tests the rounding up if decimal is more than 2 places
  def test_whenCalculateExactChangeDollarAmount10Dot003_thenReturnDenominationTypeTenIs1PennyIs1(self):
    denominationReturn: DenominationsType = {
      'hundreds': 0,
      'fifities': 0,
      'twenties': 0,
      'tens': 1,
      'fives': 0,
      'ones': 0,
      'quarters': 0,
      'dimes': 0,
      'nickels': 0,
      'pennies': 1
    }
    
    self.assertDictEqual(CalculateExactChange(10.003), denominationReturn)
  
  # DollarAmount = 186.41 (all the values added up). Should return 1 for each denomination
  def test_whenCalculateExactChangeDollarAmount186Dot41_thenReturnDenominationTypeIs1s(self):
    denominationReturn: DenominationsType = {
      'hundreds': 1,
      'fifities': 1,
      'twenties': 1,
      'tens': 1,
      'fives': 1,
      'ones': 1,
      'quarters': 1,
      'dimes': 1,
      'nickels': 1,
      'pennies': 1
    }
    
    self.assertDictEqual(CalculateExactChange(186.41), denominationReturn)

  # DollarAmount = -1 then check for an exception Raised
  def test_whenCalculateExactChangeDollarAmountNegative1_thenRaisedInvalidDollarAmountRange(self):
    self.assertRaises(CalculateExactChange(-1), InvalidDollarAmountRange)


if __name__ == '__main__':
  unittest.main()

  
  
