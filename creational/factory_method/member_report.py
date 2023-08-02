from report import Report, ReportFactory

class MemberReport(Report):
    def __init__(self, data):
        self.data = data

    def generate(self):
        # Logika untuk menghasilkan laporan anggota dari data yang diberikan
        print("Generating Member Report...")
        # Contoh: Print data anggota
        print(f"Member Data: {self.data}")

class MemberReportFactory(ReportFactory):
    def __init__(self, data):
        self.data = data

    def create_report(self):
        return MemberReport(self.data)
