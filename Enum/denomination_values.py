'''
This enumerator is USD Denomination Values in cents.
It provides an easy way to access a denomination value with a consistent and more readable format.
This should help make the code more readable when using these values.
''' 

from enum import Enum

class DenominationValues(Enum):
  '''This enumerator is USD Denomination Values in cents'''
  PENNY = 1
  NICKEL = 5
  DIME = 10
  QUARTER = 25
  ONE = 100
  FIVE = 500
  TEN = 1000
  TWENTY = 2000
  FIFTY = 5000
  HUNDRED = 10000

