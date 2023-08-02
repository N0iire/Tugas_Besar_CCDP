from loan_state import LoanState

class LoanApplication:
    def __init__(self):
        self.state = None

    def set_state(self, state: LoanState):
        self.state = state

    def process_loan(self):
        self.state.process()
