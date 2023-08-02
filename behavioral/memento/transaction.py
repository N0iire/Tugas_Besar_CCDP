from datetime import datetime

class Transaction:
    def __init__(self, amount):
        self._amount = amount
        self._timestamp = datetime.now()

    def get_amount(self):
        return self._amount

    def get_timestamp(self):
        return self._timestamp

    def __str__(self):
        return f"Transaction: Amount={self._amount}, Timestamp={self._timestamp}"
