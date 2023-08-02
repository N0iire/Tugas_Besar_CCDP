from member import Member

class IndividualMember(Member):
    def __init__(self, name, savings_balance):
        super().__init__(name)
        self.savings_balance = savings_balance

    def display(self):
        print(f"Individual Member: {self.name}, Savings Balance: {self.savings_balance}")
