'''
This enumerator is USD Denomination Values in dollars.
It provides an easy way to access a denomination value with a consistent and more readable format.
This should help make the code more readable when using these values.
''' 

from enum import Enum

class DenominationValues(Enum):
  '''This enumerator is USD Denomination Values'''
  PENNY = 0.01
  NICKEL = 0.05
  DIME = 0.10
  QUARTER = 0.25
  ONE = 1.00
  FIVE = 5.00
  TEN = 10.00
  TWENTY = 20.00
  FIFTY = 50.00
  HUNDRED = 100.00

