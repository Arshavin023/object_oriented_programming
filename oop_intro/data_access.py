# Accessing and setting data in classes

# Let's say we have a User class that defines what data a user should have


class User:
    def __init__(self, username:str, email:str, password:str):
        self.username = username
        self._email = email
        self.password = password

    def sayHiToUser(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ;)"
        )


user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@gmail.com", "abc")
user1.sayHiToUser(user2)

print(user1._email)

user1._email = "danoutlook.com"  # PROBLEM: we can set email to anything!

print(user1._email)

# SOLUTION: we need a way of controlling the way we can get and set data. Let me show you two ways: one traditional "Java"-style, and one the more modern "Python" (and C#) style.

# 1. The traditional way: make the data private and use getters and setters:

from datetime import datetime

class User2:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self._email = email
        self.isAdmin = isAdmin

    # convention: get + attr name
    def getEmail(self):
        # Advantage of getter: if we need to make changes to way data is accessed, we can do it just here -- not everywhere we are accessing email
        if self.isAdmin:
            print(f"Email accessed at {datetime.now()}")
            return self._email
        return None  # Explicitly returns None to indicate no access

    # convention: set + attr name
    def setEmail(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail


user1 = User2("dantheman", "dan@gmail.com", True)
print(user1._email)  # NAUGHTY!! As responsible Python devs, we are expected to do this:
print(user1.getEmail())  # Controlled access

user1.setEmail("dan@outlook.com")
print(user1.getEmail())

# Python’s Take on Access Modifiers
# Unlike languages such as Java or C++, which enforce strict access control (like private or protected), Python takes a more relaxed approach. In Python:

# A single underscore (_) before a name (e.g., _attribute) is a convention indicating that something is intended for internal use within the class or module. This means it’s not part of the public API, and external code shouldn’t access it directly.
# However, Python doesn’t enforce this restriction. The attribute or method is still accessible from outside the class, but it signals to developers that it’s meant to be “protected” or “internal.”

# The “Consenting Adults” Philosophy
# Guido van Rossum’s "consenting adults" philosophy highlights Python’s emphasis on developer responsibility rather than strict rules. This philosophy suggests that:

# Developers are trusted to respect the convention of not accessing underscore-prefixed attributes or methods.
# Access is not prevented, as Python assumes that developers will act responsibly and won’t misuse or access “protected” members unless absolutely necessary.

# 2. Using properties

# This is the recommended approach in python. let's see why...


class User3:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self.email = email  # this triggers the setter property
        self.isAdmin = isAdmin

    # Getter property
    @property
    def email(self):
        if self.isAdmin:
            return self._email
        print("Not admin, so can't access email")

    @email.setter
    def email(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail
        else:
            raise ValueError("Invalid email: no '@'")


user1 = User3("dantheman", "dan@gmail.com", True)
print(user1.email)
try:
    user1.email = "dayyn@gmail.com"
except ValueError as e:
    print(f"Error: {e}")

print(user1.email)

# public vs protected vs private attributes (and methods)

# static attributes and methods

# Let's say that we want to keep track of the total number of user objects that have been created. To do that, we can create a "static" attribute on the User class:


# class User4:
#     total_users_created = (
#         0  # Create a static attribute called total_users and initialise it to 0
#     )

#     def __init__(self, username, email, isAdmin=False):
#         self.username = username
#         self.email = email
#         self.isAdmin = isAdmin

#         # Whenever a new user is created, we increment the value
#         User4.total_users_created += 1

#     @property
#     def email(self):
#         if self.isAdmin:
#             return self._email
#         print("Not admin, so can't access email")

#     @email.setter
#     def email(self, newEmail):
#         if "@" in newEmail:
#             self._email = newEmail
#         else:
#             raise ValueError("Invalid email: no '@'")


# print(User4.total_users_created)
# user = User4("dantheman", "dan@gmail.com", True)
# print(User4.total_users_created)
# user2 = User4("joetheman", "joe@gmail.com", False)
# print(User4.total_users_created)
# user4 = User4("sally123", "sal@gmail.com", False)
# print(User4.total_users_created)