from loan_state import LoanState

class LoanCanceled(LoanState):
    def process(self):
        print("Pinjaman telah dibatalkan.")
