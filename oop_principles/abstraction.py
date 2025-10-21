# Abstraction: Reduce complexity by hiding unnecessary details

class EmailService:
    def send_email(self, to_address:str, subject:str, body:str):
        self.__connect_to_smtp_server()
        self.compose_email(to_address, subject, body)
        self.dispatch_email()
        self.__disconnect_from_smtp_server()

    def __connect_to_smtp_server(self):
        print("Connecting to SMTP sserver...")

    def compose_email(self, to_address:str, subject:str, body:str):
        print(f"Composing email to: {to_address}, Subject: {subject}")

    def dispatch_email(self):
        print("Sending email...")

    def __disconnect_from_smtp_server(self):
        print("Disconnecting from SMTP server...")

email_service = EmailService()
email_service.send_email("arshavin02349@gmail.com",
                            "Abstraction in OOP",
                            "This email demonstrates abstraction principle in OOP.")

