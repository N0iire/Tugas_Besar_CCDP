from abc import ABC, abstractmethod

# Abstraksi untuk pengiriman pesan
class NotificationBridge(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Implementasi khusus pengiriman pesan melalui email
class EmailNotification(NotificationBridge):
    def send(self, message: str):
        print(f"Sending email notification: {message}")

# Implementasi khusus pengiriman pesan melalui SMS
class SMSNotification(NotificationBridge):
    def send(self, message: str):
        print(f"Sending SMS notification: {message}")
