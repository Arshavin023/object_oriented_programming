# # Bad example
# class BadBankAccount:
#     def __init__(self, balance:float) -> None:
#         self.balance = balance

# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)


# Good example: We restrict the user from accessing account balance directly and only through a getter property
class BadBankAccount:
    def __init__(self) -> None:
        self.__balance = 0.0

    @property
    def balance(self):
        return self.__balance
    
    def debit(self, amount:int):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.__balance - 10 > amount:
            self.__balance -= amount
        else:
            print("Withdrawal Limit exceeded, please reduce withdrawal amount")
        
        
    
    def credit(self, amount:int):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        print("Account successfully deposited.")
        

account = BadBankAccount()
account.credit(100)
print(f"Account balance is {account.balance}")
account.debit(90)
print(f"Account balance is {account.balance}")