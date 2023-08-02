from financial_report import FinancialReportFactory
from member_report import MemberReportFactory

def main():
    financial_data = {"income": 10000, "expenses": 5000}
    member_data = {"name": "John Doe", "membership_type": "Regular"}

    # Pembuatan laporan keuangan
    financial_report_factory = FinancialReportFactory(financial_data)
    financial_report = financial_report_factory.create_report()
    financial_report.generate()

    # Pembuatan laporan anggota
    member_report_factory = MemberReportFactory(member_data)
    member_report = member_report_factory.create_report()
    member_report.generate()

if __name__ == "__main__":
    main()
