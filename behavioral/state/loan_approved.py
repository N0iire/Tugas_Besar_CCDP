from loan_state import LoanState

class LoanApproved(LoanState):
    def process(self):
        print("Pinjaman telah disetujui.")
