from typing import TypedDict

class DenominationsType(TypedDict):
  '''Data Type for Denomination Types.'''
  hundreds: int
  fifities: int
  twenties: int
  tens: int
  fives: int
  ones: int
  quarters: int
  dimes: int
  nickels: int
  pennies: int