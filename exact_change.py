from Enum.denomination_values import DenominationValues
from execptions.invalid_dollar_amount_range import InvalidDollarAmountRange
import math

def CalcDenominationQuantity(dollarAmount: float, currencyValue: DenominationValues ) -> int:
  '''Calculate the quantity of the specified currency value. 
  
    **Example:** $20.00, DenominationValues.FIVE = 4.
  
    **Paremeters:**
      dollarAmount (float): The dollar amount to divide
      currencyValue (CurrencyValue): The currency to divide by

    **Returns:**
      int: Amount of currency that will fit in the dollarAmount
  '''
  return math.floor()


def isValidDollarAmount(dollarAmount: float) -> bool:
  '''Checks for dollarAmount >= 0'''
  return dollarAmount >= 0


def CalculateExactChange(dollarAmount: float) -> dict:
  '''This function will calculate the exact amount of denominations to return for the dollarAmount. 

  **Parameters:**
    dollarAmount (float): The dollar amount (2 decimal places) to calculate denominations for. dollarAmount will be rounded up to the hundredth.
  
  **Returns:** 
    dict: dictionary of denominations and the amount of each to equal the dollarAmount. 
  '''

  # Validate dollarAmount
  if not isValidDollarAmount():
    # Raise Custom Exception.
    raise InvalidDollarAmountRange("Dollar Amount is less than zero.")

  # Default Round up to correct decimal issues. 
  dollarAmount = math.ceil(dollarAmount, 2)





  return 
