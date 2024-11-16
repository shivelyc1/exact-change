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
  # DollarAmountInCents zero
  def test_whenCalcDenominationQuantityDollarAmount0DenominationValueHUNDRED_thenReturnIs0(self):
    self.assertEqual(CalcDenominationQuantity(0, DenominationValues.HUNDRED), 0)

  # DollarAmountInCents = 10000, DenominationValue = HUNDRED
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueHUNDRED_thenReturnIs1(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.HUNDRED), 1)

  # DollarAmountInCents = 10000, DenominationValue = FIFTY
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueFIFTY_thenReturnIs2(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.FIFTY), 2)

  # DollarAmountInCents = 10000, DenominationValue = TWENTY
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueTWENTY_thenReturnIs5(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.TWENTY), 5)

  # DollarAmountInCents = 10000, DenominationValue = TEN
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueTEN_thenReturnIs10(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.TEN), 10)

  # DollarAmountInCents = 10000, DenominationValue = FIVE
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueFIVE_thenReturnIs20(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.FIVE), 20)

  # DollarAmountInCents = 10000, DenominationValue = ONE
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueONE_thenReturnIs10000(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.ONE), 100)

  # DollarAmountInCents = 10000, DenominationValue = QUARTER
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueQUARTER_thenReturnIs400(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.QUARTER), 400)

  # DollarAmountInCents = 10000, DenominationValue = DIME
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueDIME_thenReturnIs100000(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.DIME), 1000)

  # DollarAmountInCents = 10000, DenominationValue = NICKEL
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValueNICKEL_thenReturnIs2000(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.NICKEL), 2000)

  # DollarAmountInCents = 10000, DenominationValue = PENNY
  def test_whenCalcDenominationQuantityDollarAmount10000DenominationValuePENNY_thenReturnIs10000(self):
    self.assertEqual(CalcDenominationQuantity(10000, DenominationValues.PENNY), 10000)


  # CalculateExactChange() Tests
  # DollarAmountInCents = 0 then Dictionary with denomination values are all zero
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

  # DollarAmount = -1 then check for an InvalidDollarAmountRange Raised
  def test_whenCalculateExactChangeDollarAmountNegative1_thenRaisedInvalidDollarAmountRange(self):
    with self.assertRaises(InvalidDollarAmountRange):
      CalculateExactChange(-1)


if __name__ == '__main__':
  unittest.main()

  
  
