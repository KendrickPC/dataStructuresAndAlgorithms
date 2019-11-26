class CreditCard:
    # Consumer Credit Card

    def __init__(self, customer, bank, account, limit):
        """ 
        Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer.
        bank        The name of the bank.
        acnt        The account identifier
        limit       credit limit (measured in USD)
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        # REturn name of the customer.
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payments(self, amount):
        self._balance -= amount

    