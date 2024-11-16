from Enum.denomination_values import DenominationValues
from return_types.denominations_type import DenominationsType
from exceptions.invalid_dollar_amount_range import InvalidDollarAmountRange
import math

def CalcDenominationQuantity(dollarAmountInCents: int, denominationValue: DenominationValues ) -> int:
  '''Calculate the quantity of the specified denomination value. 
  
    **Example:** $20.00, DenominationValues.FIVE = 4.
  
    **Paremeters:**
      dollarAmount (int): The dollar amount to divide
      denominationValue (DenominationValue): The denomination to divide by

    **Returns:**
      int: Amount of denomination that will fit in the dollarAmount
  '''
  # Round down because we need the whole number and not the decimal value
  return math.floor(dollarAmountInCents / denominationValue.value)


def isValidDollarAmount(dollarAmount: float) -> bool:
  '''Checks for dollarAmount >= 0'''
  return dollarAmount >= 0


def CalculateExactChange(dollarAmount: float) -> DenominationsType:
  '''This function will calculate the exact amount of denominations to return for the dollarAmount. 

  **Parameters:**
    dollarAmount (float): The dollar amount (2 decimal places) to calculate denominations for. dollarAmount will be rounded up to the hundredth.
  
  **Returns:** 
    dict: dictionary of denominations and the amount of each to equal the dollarAmount. 
  '''
  
  # Validate dollarAmount
  if not isValidDollarAmount(dollarAmount):
    # Raise Custom Exception.
    raise InvalidDollarAmountRange("Dollar Amount is less than zero.")
  
  ### Ran into bug with floats where there where errors when multiplying and dividing to cause .00999999999 as a result for a number. ###
  ### Converted to cents for an integer value to eliminate this issue ###

  # Default Round up to correct decimal issues. Rounding to 2 decimal places
  dollarAmountinCents = math.ceil(dollarAmount * 100)

  # Calculate Hundreds
  hundredsQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.HUNDRED)

  # Subtract hundredsQty dollar value from dollarAmount
  dollarAmountinCents -= hundredsQty * DenominationValues.HUNDRED.value


  # Calculate Fifties
  fifitesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.FIFTY)

  # Subtract fiftiesQty dollar value from dollarAmount
  dollarAmountinCents -= fifitesQty * DenominationValues.FIFTY.value


  # Twenties Quantity
  twentiesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.TWENTY)

  dollarAmountinCents -= twentiesQty * DenominationValues.TWENTY.value


  # Tens Quantity
  tensQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.TEN)

  dollarAmountinCents -= tensQty * DenominationValues.TEN.value

 
  # Fives Quantity
  fivesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.FIVE)

  dollarAmountinCents -= fivesQty * DenominationValues.FIVE.value


  # Ones Quantity
  onesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.ONE)

  dollarAmountinCents -= onesQty * DenominationValues.ONE.value


  # Quarter Quantity
  quartersQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.QUARTER)

  dollarAmountinCents -= quartersQty * DenominationValues.QUARTER.value


  # Dimes Quantity
  dimesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.DIME)

  dollarAmountinCents -= dimesQty * DenominationValues.DIME.value


  # Nickels Quantity
  nickelsQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.NICKEL)

  dollarAmountinCents -= nickelsQty * DenominationValues.NICKEL.value


  # Pennies Quantity
  penniesQty = CalcDenominationQuantity(dollarAmountinCents, DenominationValues.PENNY)

  dollarAmountinCents -= penniesQty * DenominationValues.PENNY.value


  return {
    "hundreds": hundredsQty,
    "fifities": fifitesQty,
    "twenties": twentiesQty,
    "tens" : tensQty,
    "fives" : fivesQty,
    "ones" : onesQty,
    "quarters" : quartersQty,
    "dimes" : dimesQty,
    "nickels" : nickelsQty,
    "pennies" : penniesQty
  }
