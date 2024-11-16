from Enum.denomination_values import DenominationValues
from return_types.denominations_type import DenominationsType
from exceptions.invalid_dollar_amount_range import InvalidDollarAmountRange
import math

def CalcDenominationQuantity(dollarAmount: float, denominationValue: DenominationValues ) -> int:
  '''Calculate the quantity of the specified denomination value. 
  
    **Example:** $20.00, DenominationValues.FIVE = 4.
  
    **Paremeters:**
      dollarAmount (float): The dollar amount to divide
      denominationValue (DenominationValue): The denomination to divide by

    **Returns:**
      int: Amount of denomination that will fit in the dollarAmount
  '''
  # Round down because we need the whole number and not the decimal value
  return math.floor(dollarAmount / denominationValue.value)


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

  # Default Round up to correct decimal issues. Rounding to 2 decimal places
  dollarAmount = math.ceil(dollarAmount * 100) / 100

  # Calculate Hundreds
  hundredsQty = CalcDenominationQuantity(dollarAmount, DenominationValues.HUNDRED)

  # Subtract hundredsQty dollar value from dollarAmount
  dollarAmount -= hundredsQty * DenominationValues.HUNDRED.value


  # Calculate Fifties
  fifitesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.FIFTY)

  # Subtract fiftiesQty dollar value from dollarAmount
  dollarAmount -= fifitesQty * DenominationValues.FIFTY.value


  # Twenties Quantity
  twentiesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.TWENTY)

  dollarAmount -= twentiesQty * DenominationValues.TWENTY.value


  # Tens Quantity
  tensQty = CalcDenominationQuantity(dollarAmount, DenominationValues.TEN)

  dollarAmount -= tensQty * DenominationValues.TEN.value

 
  # Fives Quantity
  fivesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.FIVE)

  dollarAmount -= fivesQty * DenominationValues.FIVE.value


  # Ones Quantity
  onesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.ONE)

  dollarAmount -= onesQty * DenominationValues.ONE.value


  # Quarter Quantity
  quartersQty = CalcDenominationQuantity(dollarAmount, DenominationValues.QUARTER)

  dollarAmount -= quartersQty * DenominationValues.QUARTER.value


  # Dimes Quantity
  dimesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.DIME)

  dollarAmount -= dimesQty * DenominationValues.DIME.value


  # Nickels Quantity
  nickelsQty = CalcDenominationQuantity(dollarAmount, DenominationValues.NICKEL)

  dollarAmount -= nickelsQty * DenominationValues.NICKEL.value


  # Pennies Quantity
  penniesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.PENNY)

  dollarAmount -= penniesQty * DenominationValues.PENNY.value


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
