# Object-Oriented Programming Demonstration

A Python demonstration showcasing core Object-Oriented Programming (OOP) concepts including **Inheritance**, **Polymorphism**, and **Encapsulation** through a practical smartphone device example.

## 📋 Overview

This project demonstrates fundamental OOP principles using a parent `Device` class and a child `Smartphone` class. The code shows how inheritance allows code reuse, polymorphism enables method overriding, and encapsulation protects sensitive data like PIN codes.

## 🎯 Learning Objectives

By studying this code, you'll understand:
- **Inheritance**: How child classes inherit properties and methods from parent classes
- **Polymorphism**: How child classes can override parent methods with specialized behavior
- **Encapsulation**: How to protect sensitive data using private attributes
- **Constructor chaining**: Using `super()` to call parent constructors
- **Method overriding**: Customizing inherited behavior for specific use cases

## 📁 Project Structure

```
├── smartphone_demo.py    # Main demonstration file
└── README.md            # This documentation
```

## 🔧 Classes and Methods

### Device (Parent Class)
The base class representing any generic device.

**Attributes:**
- `brand`: Device manufacturer (e.g., "Apple", "Samsung")
- `model`: Device model name (e.g., "iPhone 15", "Galaxy S24")

**Methods:**
- `__init__(brand, model)`: Initialize device with brand and model
- `power_on()`: Generic power-on message

### Smartphone (Child Class)
Inherits from Device and adds smartphone-specific functionality.

**Additional Attributes:**
- `storage_gb`: Storage capacity in gigabytes
- `battery_level`: Current battery percentage (starts at 100%)
- `_pin_code`: Private PIN code for device security

**Methods:**
- `__init__(brand, model, storage_gb)`: Initialize smartphone with inherited and new attributes
- `power_on()`: **Overridden** method with smartphone-specific boot message
- `make_call(number)`: Simulate making a phone call
- `charge(percent)`: Increase battery level by specified percentage
- `install_app(app_name)`: Simulate app installation
- `set_pin_code(pin)`: Set device PIN code (encapsulation)
- `unlock(pin)`: Attempt to unlock device with PIN

## 🚀 How to Run

1. **Prerequisites**: Python 3.6 or higher installed on your system

2. **Run the demonstration**:
   ```bash
   python smartphone_demo.py
   ```

3. **Expected Output**:
   ```
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
   ```

## 💡 Key OOP Concepts Demonstrated

### 1. Inheritance
```python
class Smartphone(Device):  # Smartphone inherits from Device
    def __init__(self, brand, model, storage_gb):
        super().__init__(brand, model)  # Call parent constructor
```

### 2. Polymorphism
```python
# Device class
def power_on(self):
    print(f"{self.brand} {self.model} is now powered on.")

# Smartphone class (overridden)
def power_on(self):
    print(f"📱 {self.model} is booting up... Welcome!")
```

### 3. Encapsulation
```python
self._pin_code = None  # Private attribute (convention with underscore)

def set_pin_code(self, pin):  # Controlled access to private data
    self._pin_code = pin
```

## 🛠️ Customization Ideas

You can extend this demonstration by:

1. **Adding more device types**: Create `Laptop`, `Tablet`, or `Smartwatch` classes
2. **Implementing more encapsulation**: Add getter/setter methods with `@property`
3. **Adding abstract methods**: Use `abc` module to create abstract base classes
4. **Error handling**: Add try-catch blocks for invalid inputs
5. **Data validation**: Ensure PIN codes meet security requirements

## 📚 Educational Notes

- **Private attributes**: Python uses naming conventions (`_attribute`) rather than true private variables
- **Method Resolution Order (MRO)**: Python searches for methods in child class first, then parent
- **super()**: Best practice for calling parent class methods in inheritance hierarchies
- **Polymorphism benefits**: Same interface (`power_on()`) works differently for different objects

## 🤝 Contributing

This is an educational demonstration. Feel free to:
- Add more device types
- Implement additional OOP patterns
- Improve error handling
- Add unit tests

## 📄 License

This code is provided for educational purposes. Feel free to use and modify for learning OOP concepts.

---

*This demonstration uses Kenyan phone number formats (+254) as examples. Replace with your local format as needed.*