from loan_state import LoanState

class LoanRejected(LoanState):
    def process(self):
        print("Pinjaman telah ditolak.")
