

class InvalidDollarAmountRange(Exception):
  '''Invalid Dollar Amount Range Exception. This should be thrown when the dollar amount is < 0.'''

  def __init__(self, message):
    self.message = message
    super().__init__(self.message)