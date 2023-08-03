from message import Message, MessageSender

# Implementasi khusus pesan SMS
class SMS(Message):
    def send(self, recipient, content):
        print(f"Sending SMS to {recipient}: {content}")

# Implementasi khusus pengirim SMS
class SMSSender(MessageSender):
    def send_message(self, recipient, content):
        print(f"Sending SMS to {recipient}: {content}")
