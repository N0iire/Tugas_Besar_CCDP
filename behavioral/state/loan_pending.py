from loan_state import LoanState

class LoanPending(LoanState):
    def process(self):
        print("Proses pinjaman sedang menunggu persetujuan.")
