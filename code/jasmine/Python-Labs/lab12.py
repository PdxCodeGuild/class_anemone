

##ATM Lab12
from decimal import Decimal

## Class object for ATM
class ATM(object):
    ##init funtion to initialize the account object
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        #if balance is less than 0, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial Balance must be >= to 0.00.')

    
    #?
