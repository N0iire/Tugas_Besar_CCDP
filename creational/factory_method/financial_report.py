from report import Report, ReportFactory

class FinancialReport(Report):
    def __init__(self, data):
        self.data = data

    def generate(self):
        # Logika untuk menghasilkan laporan keuangan dari data yang diberikan
        print("Generating Financial Report...")
        # Contoh: Print data keuangan
        print(f"Financial Data: {self.data}")

class FinancialReportFactory(ReportFactory):
    def __init__(self, data):
        self.data = data

    def create_report(self):
        return FinancialReport(self.data)
