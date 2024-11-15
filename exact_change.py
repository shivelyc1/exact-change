from Enum.denomination_values import DenominationValues
from execptions.invalid_dollar_amount_range import InvalidDollarAmountRange
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

  # Calculate Hundreds
  hundredsQty = CalcDenominationQuantity(dollarAmount, DenominationValues.HUNDRED)

  # Subtract hundredsQty dollar value from dollarAmount
  dollarAmount -= hundredsQty * DenominationValues.HUNDRED


  # Calculate Fifties
  fifitesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.FIFTY)

  # Subtract fiftiesQty dollar value from dollarAmount
  dollarAmount -= fifitesQty * DenominationValues.FIFTY

  
  twentiesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.TWENTY)

  dollarAmount -= twentiesQty * DenominationValues.TWENTY


  tensQty = CalcDenominationQuantity(dollarAmount, DenominationValues.TEN)

  dollarAmount -= tensQty * DenominationValues.TEN


  fivesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.FIVE)

  dollarAmount -= fivesQty * DenominationValues.FIVE

  
  onesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.ONE)

  dollarAmount -= onesQty * DenominationValues.ONE

  
  quartersQty = CalcDenominationQuantity(dollarAmount, DenominationValues.QUARTER)

  dollarAmount -= quartersQty * DenominationValues.QUARTER


  dimesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.DIME)

  dollarAmount -= dimesQty * DenominationValues.DIME


  nickelsQty = CalcDenominationQuantity(dollarAmount, DenominationValues.NICKEL)

  dollarAmount -= nickelsQty * DenominationValues.NICKEL


  penniesQty = CalcDenominationQuantity(dollarAmount, DenominationValues.PENNY)

  dollarAmount -= penniesQty * DenominationValues.PENNY

  if dollarAmount != 0:
    print(f"DollarAmount: {dollarAmount}")





  

  return {
    
  }
