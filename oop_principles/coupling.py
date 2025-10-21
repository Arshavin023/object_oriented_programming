# Coupling: This refers to the degree of dependency between different modules or classes.

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message:str):
        pass

class EmailService(NotificationService):
    def send_notification(self, message:str):
        print(f"Sending email: {message}")

class MobileService(NotificationService):
    def send_notification(self, message:str):
        print(f"Sending text message: {message}")

class Order:
    def __init__(self, notification_service:NotificationService):
        self.notification_service=notification_service
        
    def create(self):
        return self.notification_service.send_notification("Hi, your order is being processed and would be delivered in  working days")

order = Order(MobileService())
order.create()

order2 = Order(EmailService())
order2.create()