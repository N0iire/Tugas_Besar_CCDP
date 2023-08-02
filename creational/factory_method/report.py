from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class ReportFactory(ABC):
    @abstractmethod
    def create_report(self):
        pass
