from notification_bridge import NotificationBridge, EmailNotification, SMSNotification

class NotificationService:
    def __init__(self, notification_impl: NotificationBridge):
        self._notification_impl = notification_impl

    def send_notification(self, message: str):
        self._notification_impl.send(message)

if __name__ == "__main__":
    # Menggunakan EmailNotification sebagai implementasi
    email_notification = EmailNotification()
    notification_service = NotificationService(email_notification)
    notification_service.send_notification("Hello, this is an email notification!")

    print("")

    # Menggunakan SMSNotification sebagai implementasi
    sms_notification = SMSNotification()
    notification_service = NotificationService(sms_notification)
    notification_service.send_notification("Hello, this is an SMS notification!")
