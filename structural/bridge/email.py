from message import Message, MessageSender

# Implementasi khusus pesan Email
class Email(Message):
    def send(self, recipient, content):
        print(f"Sending Email to {recipient}: {content}")

# Implementasi khusus pengirim Email
class EmailSender(MessageSender):
    def send_message(self, recipient, content):
        print(f"Sending Email to {recipient}: {content}")
