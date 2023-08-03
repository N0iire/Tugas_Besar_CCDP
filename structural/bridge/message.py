from abc import ABC, abstractmethod

# Abstraksi untuk pesan
class Message(ABC):
    def __init__(self, sender):
        self._sender = sender

    @abstractmethod
    def send(self, recipient, content):
        pass

# Abstraksi untuk pengirim pesan
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, content):
        pass
