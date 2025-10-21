class Owner:
    def __init__(self, name:str, address:str, contact_number:str) -> None:
        self.name=name 
        self.address=address 
        self.contact_number=contact_number

class Dog:
    def __init__(self, name:str, breed:str, owner:Owner) -> None:
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print(f"{self.name} of {self.breed} Whoof whoof")

class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name=name 
        self.age=age
        
    def greet(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

class User:
    def __init__(self, username:str, email:str, password:str) -> None:
        self.username=username
        self._email=email
        self.password=password

    def clean_email(self):
        return self._email.lower().strip()
    
    # def say_hi_to_user(self, user):
    #     print(f"""Sending message to {user.username}: Hi {user.username}, it's {self.username}""")

owner1 = Owner("Uche","11A Along Mango Tree, Dutse Katampe","08167164325")

dog1 = Dog("Bingo","German Shephered",owner1)
dog1.bark()
print(dog1.owner.name)
print(dog1.owner.address)
# print(dog1.name)
# print(dog1.breed)

person1 = Person("Uche",34)
person1.greet()

user1 = User("Jude","nnodimuche@yahoo.com","Constant7777@")
user2 = User("Uche", " uchejUdennodim@gmail.com ", "Neymar02349@")

print(user2.clean_email())