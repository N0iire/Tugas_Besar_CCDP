from loan_application import LoanApplication
from loan_pending import LoanPending
from loan_approved import LoanApproved
from loan_rejected import LoanRejected
from loan_canceled import LoanCanceled

if __name__ == "__main__":
    loan_app = LoanApplication()

    # Memulai dengan status pinjaman dalam keadaan menunggu persetujuan
    loan_app.set_state(LoanPending())
    loan_app.process_loan()

    # Ubah status pinjaman menjadi disetujui
    loan_app.set_state(LoanApproved())
    loan_app.process_loan()

    # Ubah status pinjaman menjadi ditolak
    loan_app.set_state(LoanRejected())
    loan_app.process_loan()

    # Ubah status pinjaman menjadi dibatalkan
    loan_app.set_state(LoanCanceled())
    loan_app.process_loan()
