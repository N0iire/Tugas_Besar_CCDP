from message import Message
from sms import SMS, SMSSender
from email import Email, EmailSender

if __name__ == "__main__":
    # Menggunakan pesan SMS
    sms_sender = SMSSender()
    sms_message = SMS(sms_sender)
    sms_message.send("08123456789", "Hello, this is an SMS message.")

    # Menggunakan pesan Email
    email_sender = EmailSender()
    email_message = Email(email_sender)
    email_message.send("recipient@example.com", "Hello, this is an Email message.")
