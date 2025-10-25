from enum import Enum 
from abc import ABC, abstractmethod
# Bad Example of State Pattern: Violates Open/Closed Principle
# class DocumentStates(Enum):
#     DRAFT = 1
#     MODERATION = 2
#     PUBLISHED = 3

# class UserRoles(Enum):
#     READER = 1
#     EDITOR = 2
#     ADMIN = 3

# class Document:
#     def __init__(self, state: DocumentStates, current_user_role:UserRoles):
#         self.state = state
#         self.current_user_role = current_user_role

#     def publish(self) -> None:
#         if self.state == DocumentStates.DRAFT:
#             self.state = DocumentStates.MODERATION
#         elif (self.state == DocumentStates.MODERATION 
#               and self.current_user_role == UserRoles.ADMIN):
#             self.state = DocumentStates.PUBLISHED
#         elif self.state == DocumentStates.PUBLISHED:
#             # Do Nothing
#             pass

# Good Example of State Pattern: Adheres to Open/Closed Principle
class DocumentStates(Enum):
    DRAFT = 1
    MODERATION = 2
    PUBLISHED = 3

class UserRoles(Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3

class Document:
    def __init__(self, current_user_role:UserRoles):
        self.state = DraftState(self)
        self.current_user_role = current_user_role

    def publish(self) -> None:
        self.state.publish()
        #     pass

class State(ABC):
    @abstractmethod
    def publish(self) -> None:
        pass    

class DraftState(State):
    def __init__(self, document:Document):
        self.__document = document

    def publish(self) -> None:
        print("Transitioning from DRAFT to MODERATION")
        self.__document.state = ModerationState(self.__document)
        
class ModerationState(State):
    def __init__(self, document:Document):
        self.__document = document

    def publish(self) -> None:
        if self.__document.current_user_role == UserRoles.ADMIN:
            print("Transitioning from MODERATION to PUBLISHED")
            self.__document.state = PublishedState(self.__document)
        else:
            print("Only ADMIN can publish from MODERATION state.")

class PublishedState(State):
    def __init__(self, document:Document):
        self.__document = document

    def publish(self) -> None:
        print("Document is already PUBLISHED. No further transitions.")
        
doc = Document(current_user_role=UserRoles.EDITOR)
print(f"Initial Document State: {doc.state.__class__.__name__}")
doc.publish()
# print(f"Document State after first publish attempt by EDITOR: {doc.state.__class__.__name__}")
doc.publish()
# print(f"Document State after second publish attempt by ADMIN: {doc.state.__class__.__name__}")
doc.publish()

# Note; State Patterns could be overkill for simple scenarios e.g., two. Use judiciously.