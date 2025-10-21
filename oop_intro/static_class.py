class User:
    user_count:float =0
    def __init__(self, username:str, email:str):
        self.username = username
        self.email = email
        User.user_count += 1
    
    def display_user(self):
        print(f"Username: {self.username}. Email: {self.email}")

print(User.user_count)
user1 = User("Arshavin023","nnodimuche@yahoo.com")
print(user1.user_count)
user2 = User("Neymar023","uchejudennodim@gmail.com")

print(User.user_count)
print(user2.user_count)

# When to static vs instance attributes
# Static attributes are used for counters cos they are at class level while instance attributes are unique to each object (instance of the class)

# Static vs instance Method
# A static method is a method that belongs to the class itself rather than the object (instance of the object)

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner:str, balance:float=0):
        self.owner = owner 
        self.__balance = balance
    
    def balance(self):
        return self.__balance
    
    def transaction(self, amount:float, transaction_type:str):
        if self.__is_valid_amount(amount):
            if transaction_type=='debit':
                if self.__balance > amount:
                    self.__balance -= amount
                    self.__log_transaction(transaction_type,amount)
                else:
                    print(f"Trasactional failed due to insufficient funds")

            else:
                self.__balance += amount
                self.__log_transaction(transaction_type, amount)
        else:
            print("Deposit amount must be positive.")
    
    # double underscores shows it's a private attribute and would throw an error when it's accessed outside the class
    def __is_valid_amount(self, amount:float):
        return amount > 0
    
    def __log_transaction(self, transaction_type:str, amount:float):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self.__balance}")
    @staticmethod
    def is_valid_interest_rate(rate:float):
        return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.transaction(300,'debit')
print(account.balance())
# print(BankAccount.is_valid_interest_rate(2))
# print(BankAccount.is_valid_interest_rate(10))