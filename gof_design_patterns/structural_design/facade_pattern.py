from abc import ABC, abstractmethod
from typing import List 

# # Bad Example: Complex order processing without a facade.
# class OrderRequest:
#     def __init__(self):
#         self.name = "danny"
#         self.card_number = "1234-5678-9876-5432"
#         self.amount = 250.0
#         self.address = "123 Main St, City, Country" 
#         self.items_ids = ["123", "456", "789"]

# class Authenticator:
#     def authenticate(self, name: str, card_number: str) -> bool:
#         print(f"Authenticating {name} with card {card_number}")
#         return True

# class Inventory:
#     def check_and_reserve(self, items_ids: str) -> bool:
#         print(f"Checking and reserving items: {items_ids}")
#         return True
#     def reduce_inventory(self, items_ids:str, amount:int) -> None:
#         print(f"Reducing inventory for items: {items_ids} by {amount}")
    
# class Payment:
#     def __init__(self,name:str, card_number:str, amount:float) -> None:
#         self.__name = name
#         self.__card_number = card_number
#         self.__amount = amount
#     def pay(self) -> bool:
#         print(f"Processing payment of {self.__amount} for {self.__name} using card {self.__card_number}")
#         return True

# class OrderFulfillment:
#     def __init__(self, inventory:Inventory) -> None:
#         self.__inventory = inventory
#     def fulfill(self, name:str, address: str, items_ids: List[str]) -> None:
#         print("Inserting order into database")
#         for item_id in items_ids:
#             self.__inventory.reduce_inventory(item_id, 1)

# # Order request facade
# order_request = OrderRequest()
# auth = Authenticator()
# auth.authenticate(order_request.name, order_request.card_number)
# inventory = Inventory()
# for item_id in order_request.items_ids:
#     inventory.check_and_reserve(item_id)
# payment = Payment(order_request.name, order_request.card_number, order_request.amount)
# payment.pay()
# order_fulfillment = OrderFulfillment(inventory)
# order_fulfillment.fulfill(order_request.name, order_request.address, order_request.items_ids)   


# Good example: Complex order processing with a facade.
class OrderRequest:
    def __init__(self):
        self.name = "danny"
        self.card_number = "1234-5678-9876-5432"
        self.amount = 250.0
        self.address = "123 Main St, City, Country" 
        self.items_ids = ["123", "456", "789"]

class Authenticator:
    def authenticate(self, name: str, card_number: str) -> bool:
        print(f"Authenticating {name} with card {card_number}")
        return True

class Inventory:
    def check_and_reserve(self, items_ids: str) -> bool:
        print(f"Checking and reserving items: {items_ids}")
        return True
    def reduce_inventory(self, items_ids:str, amount:int) -> None:
        print(f"Reducing inventory for items: {items_ids} by {amount}")
    
class Payment:
    def __init__(self,name:str, card_number:str, amount:float) -> None:
        self.__name = name
        self.__card_number = card_number
        self.__amount = amount
    def pay(self) -> bool:
        print(f"Processing payment of {self.__amount} for {self.__name} using card {self.__card_number}")
        return True

class OrderFulfillment:
    def __init__(self, inventory:Inventory) -> None:
        self.__inventory = inventory
    def fulfill(self, name:str, address: str, items_ids: List[str]) -> None:
        print("Inserting order into database")
        for item_id in items_ids:
            self.__inventory.reduce_inventory(item_id, 1)

class OrderService:
    """
    The Facade pattern, ensuring the correct transactional order: 
    Auth -> Reserve -> Fulfill -> Charge.
    """
    def create(self, order_request: OrderRequest) -> None:
        print("--- Starting Order Processing ---")
        
        # 1. Authentication
        auth = Authenticator()
        if not auth.authenticate(order_request.name, order_request.card_number):
            raise Exception("Authentication failed")

        # 2. Inventory Check and Reservation
        inventory = Inventory()
        for item_id in order_request.items_ids:
        # Note: check_and_reserve should be called once with the full list
            if not inventory.check_and_reserve(item_id):
                raise Exception("Inventory check failed. Items unavailable.")
        
        # 3. FULFILLMENT / STOCK COMMITMENT (MUST run before final charge)
        order_fulfillment = OrderFulfillment(inventory)
        order_fulfillment.fulfill(
            order_request.name, 
            order_request.address, 
            order_request.items_ids
        )
        
        # 4. FINAL PAYMENT/CHARGE (Only if fulfillment was successful)
        payment = Payment(order_request.name, order_request.card_number, order_request.amount)
        if not payment.pay():
            # If payment fails here, we must trigger an Inventory rollback/unreserve
            raise Exception("Final payment capture failed.")

        print("--- Order Successfully Completed and Charged ---")

# Order request facade
order_request = OrderRequest()
order_service = OrderService()
order_service.create(order_request)