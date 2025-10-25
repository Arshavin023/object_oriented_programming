# Abstract Factory Patterm: is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes, 
# promoting encaptulation and allowing for the creation of object families that can vary independently from the clients that use them.

from abc import ABC, abstractmethod
from enum import Enum

# # Bad example without Abstract Factory Pattern
# class OperatingSystemType(Enum):
#     WINDOWS = "Windows"
#     MAC = "Mac"

# class UIComponent(ABC):
#     @abstractmethod
#     def render(self):
#         pass

# class Checkbox(UIComponent):
#     @abstractmethod
#     def on_select(self):
#         pass
    
# class Button(UIComponent):
#     @abstractmethod
#     def on_click(self):
#         pass

# # Windows Components
# class WindowsButton(Button):
#     def render(self):
#         print("Windows Render Button")
#     def on_click(self):
#         print("Windows Button Clicked")

# class WindowsCheckbox(Checkbox):
#     def render(self):
#         print("Windows Render Checkbox")
#     def on_select(self):
#         print("Windows Checkbox Selected")

# # Mac Components
# class MacButton(Button):
#     def render(self):
#         print("Mac Render Button")
#     def on_click(self):
#         print("Mac Button Clicked")

# class MacCheckbox(Checkbox):
#     def render(self):
#         print("Mac Render Checkbox")
#     def on_select(self):
#         print("Mac Checkbox Selected")


# # Our application classes
# class UserSettingsForm():
#     def render(self, os:OperatingSystemType):
#         if os == OperatingSystemType.WINDOWS:
#             button = WindowsButton()
#             checkbox = WindowsCheckbox()
#         elif os == OperatingSystemType.MAC:
#             button = MacButton()
#             checkbox = MacCheckbox()
#         else:
#             raise ValueError("Unsupported Operating System")

#         button.render()
#         checkbox.render()


# Good example with Abstract Factory Pattern
class OperatingSystemType(Enum):
    WINDOWS = "Windows"
    MAC = "Mac"

class UIComponent(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(UIComponent):
    @abstractmethod
    def on_select(self):
        pass
    
class Button(UIComponent):
    @abstractmethod
    def on_click(self):
        pass

class UIComponentFactory(ABC):
    @abstractmethod
    def create_button(self) -> 'Button':
        pass

    @abstractmethod
    def create_checkbox(self) -> 'Checkbox':
        pass

# Windows Components
class WindowsButton(Button):
    def render(self):
        print("Windows Render Button")
    def on_click(self):
        print("Windows Button Clicked")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("Windows Render Checkbox")
    def on_select(self):
        print("Windows Checkbox Selected")

class WindowsUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
    
# Mac Components
class MacButton(Button):
    def render(self):
        print("Mac Render Button")
    def on_click(self):
        print("Mac Button Clicked")

class MacCheckbox(Checkbox):
    def render(self):
        print("Mac Render Checkbox")
    def on_select(self):
        print("Mac Checkbox Selected")

class MacUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button:
        return MacButton()
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Our application classes
class UserSettingsForm():
    def render(self, ui_component_factory: UIComponentFactory):
        ui_component_factory.create_checkbox().render()
        ui_component_factory.create_button().render()

os = OperatingSystemType.WINDOWS
ui_component_factory: UIComponentFactory

if os == OperatingSystemType.WINDOWS:
    ui_component_factory = WindowsUIComponentFactory()
elif os == OperatingSystemType.MAC:
    ui_component_factory = MacUIComponentFactory()
else:
    raise ValueError("Unsupported Operating System")

UserSettingsForm().render(ui_component_factory)