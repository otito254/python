# ==========================================================
# Object-Oriented Programming Demonstration
# Inheritance, Polymorphism, and Optional Encapsulation
# ==========================================================

class Device:
    """Parent class representing a generic device."""

    def __init__(self, brand, model):
        """Initialize the brand and model attributes."""
        self.brand = brand
        self.model = model

    def power_on(self):
        """Generic power-on message."""
        print(f"{self.brand} {self.model} is now powered on.")


class Smartphone(Device):
    """Child class representing a smartphone."""

    def __init__(self, brand, model, storage_gb):
        """
        Initialize smartphone attributes.
        Calls the Device constructor for brand & model,
        adds storage capacity, battery, and optional PIN.
        """
        super().__init__(brand, model)
        self.storage_gb = storage_gb
        self.battery_level = 100
        self._pin_code = None  # Encapsulated (private) attribute

    # ---------- Polymorphism ----------
    def power_on(self):
        """Override the Device power_on method."""
        print(f"📱 {self.model} is booting up... Welcome!")

    # ---------- Additional Smartphone Behaviors ----------
    def make_call(self, number):
        """Simulate making a phone call."""
        print(f"Calling {number}...")

    def charge(self, percent):
        """Charge the phone battery by the given percent."""
        old_level = self.battery_level
        self.battery_level = min(100, self.battery_level + percent)
        print(f"Battery charged from {old_level}% to {self.battery_level}%.")

    def install_app(self, app_name):
        """Simulate installing an app."""
        print(f"Installing '{app_name}'... Done!")

    # ---------- Encapsulation Features ----------
    def set_pin_code(self, pin):
        """Set the phone's PIN code."""
        self._pin_code = pin
        print("PIN code has been set.")

    def unlock(self, pin):
        """Check entered PIN and unlock if correct."""
        if self._pin_code is None:
            print("No PIN set. Device unlocked.")
        elif pin == self._pin_code:
            print("PIN correct. Device unlocked!")
        else:
            print("Incorrect PIN. Access denied.")


# ==========================================================
# Testing / Demonstration
# ==========================================================

if __name__ == "__main__":

    # Create two Smartphone objects with different attributes
    phone1 = Smartphone("Apple", "iPhone 15", 256)
    phone2 = Smartphone("Samsung", "Galaxy S24", 512)

    # Demonstrate polymorphism
    phone1.power_on()  # Calls overridden Smartphone method
    phone2.power_on()

    print("\n--- Demonstrating Features for Phone 1 ---")
    phone1.make_call("+254700123456")
    phone1.charge(15)
    phone1.install_app("Slack")

    # Optional PIN feature
    phone1.set_pin_code("1234")
    phone1.unlock("1111")  # Wrong PIN
    phone1.unlock("1234")  # Correct PIN

    print("\n--- Demonstrating Features for Phone 2 ---")
    phone2.make_call("+254711987654")
    phone2.charge(5)
    phone2.install_app("Zoom")
    phone2.unlock("0000")  # No PIN set


"""
================= Sample Output =================

📱 iPhone 15 is booting up... Welcome!
📱 Galaxy S24 is booting up... Welcome!

--- Demonstrating Features for Phone 1 ---
Calling +254700123456...
Battery charged from 100% to 100%.
Installing 'Slack'... Done!
PIN code has been set.
Incorrect PIN. Access denied.
PIN correct. Device unlocked!

--- Demonstrating Features for Phone 2 ---
Calling +254711987654...
Battery charged from 100% to 100%.
Installing 'Zoom'... Done!
No PIN set. Device unlocked.
=================================================
"""
