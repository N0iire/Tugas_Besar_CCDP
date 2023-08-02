from transaction import Transaction
from transaction_caretaker import TransactionCaretaker

class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
        return Transaction(amount)

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return Transaction(-amount)
        return None

    def get_balance(self):
        return self._balance

    def create_memento(self):
        return self._balance

    def restore(self, memento):
        self._balance = memento

if __name__ == "__main__":
    bank_account = BankAccount()
    caretaker = TransactionCaretaker()

    # Transaksi 1
    deposit_1 = bank_account.deposit(1000)
    caretaker.add_memento(bank_account.create_memento())
    print(f"Balance: {bank_account.get_balance()}")

    # Transaksi 2
    deposit_2 = bank_account.deposit(500)
    caretaker.add_memento(bank_account.create_memento())
    print(f"Balance: {bank_account.get_balance()}")

    # Transaksi 3
    withdraw_1 = bank_account.withdraw(200)
    if withdraw_1:
        caretaker.add_memento(bank_account.create_memento())
        print(f"Balance: {bank_account.get_balance()}")
    else:
        print("Insufficient funds for withdrawal.")

    # Rollback to Transaksi 2
    bank_account.restore(caretaker.get_memento(1))
    print(f"Balance after rollback: {bank_account.get_balance()}")
