# Single Responsible Principle (SRP) states that a class should have only one reason to change.
# This means that a class should only have one job or responsibility.

# Bad Example:
# class EmailSender:
#     def send(self, recipient:str, message:str):
#         # Code to send email
#         print(f"Sending email to {recipient}: {message}")

# class User:
#     def __init__(self, username:str, email:str):
#         self.username = username
#         self.email = email

#     def register(self):
#         # Code to register user
#         print(f"Registering user: {self.username}")
#         email_sender = EmailSender()
#         email_sender.send(self.email, f"Welcome to our platform {self.username}!")

# user = User("Arshavin023", "uchejudennodim@gmail.com")
# user.register()

# Good Example: 
class EmailSender:
    def send(self, recipient:str, message:str):
        # Code to send email
        print(f"Sending email to {recipient}: {message}")

class User:
    def __init__(self, username:str, email:str):
        self.username = username
        self.email = email

class UserService:
    def register(self, user:User):
        print(f"Registering user: {user.username}")
        email_sender = EmailSender()
        email_sender.send(user.email, f"Welcome to our platform {user.username}!")

    def update(self, user:User, new_email:str):
        print(f"Updating user profile for: {user.username}")
        user.email = new_email
    
    def delete(self, user:User):
        print(f"Deleting user: {user.username}")    

user = User("Arshavin023", "nnodimuche@yahoo.com")
user_service = UserService()
user_service.register(user)
user_service.update(user, "uchejudennodim@gmail.com")
print(user.email)
user_service.delete(user)

# Although the UserService class has multiple methods, it is still adhering to the Single Responsibility Principle
# because all methods are related to user management. Each class has a single responsibility:
# - EmailSender is responsible for sending emails.
# - User is responsible for representing user data.
# - UserService is responsible for user-related operations like registration, updating, and deletion.   
# - It should be stateless, user data is passed as parameters to its methods and not stored as instance attributes in UserService.