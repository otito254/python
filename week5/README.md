# Object-Oriented Programming Demonstration

A comprehensive Python demonstration showcasing the four pillars of Object-Oriented Programming: **Inheritance**, **Polymorphism**, **Encapsulation**, and **Abstraction**.

## 📋 Table of Contents

- [Overview](#overview)
- [Features Demonstrated](#features-demonstrated)
- [Code Structure](#code-structure)
- [Usage](#usage)
- [Examples](#examples)
- [Key Concepts Explained](#key-concepts-explained)
- [Requirements](#requirements)
- [License](#license)

## 🎯 Overview

This project contains two practical examples that demonstrate core OOP principles:

1. **Device/Smartphone Hierarchy** - Shows inheritance, polymorphism, and encapsulation
2. **Vehicle Variants** - Demonstrates polymorphism with different vehicle types

## ✨ Features Demonstrated

### 🏗️ Inheritance
- **Device → Smartphone**: Smartphone inherits from Device base class
- **Vehicle → Car/ElectricCar/SportsCar**: Multiple vehicle types inherit from Vehicle

### 🔄 Polymorphism
- Method overriding: `power_on()` behaves differently for Device vs Smartphone
- Same interface, different behavior: All vehicles have `move()` but each moves differently

### 🔒 Encapsulation
- Private attribute: `_pin_code` in Smartphone class
- Controlled access through `set_pin_code()` and `unlock()` methods
- Data hiding and protection of internal state

### 📱 Real-World Functionality
- Battery management and charging
- Phone calls and app installation
- PIN code security system
- Vehicle movement simulation

## 📁 Code Structure

```
├── Device (Base Class)
│   ├── __init__(brand, model)
│   └── power_on()
│
├── Smartphone (Inherits from Device)
│   ├── __init__(brand, model, storage_gb)
│   ├── power_on() [Overridden]
│   ├── make_call()
│   ├── charge()
│   ├── install_app()
│   ├── set_pin_code()
│   └── unlock()
│
├── Vehicle (Base Class)
│   ├── __init__(name)
│   └── move()
│
├── Car (Inherits from Vehicle)
│   └── move() [Overridden]
│
├── ElectricCar (Inherits from Vehicle)
│   └── move() [Overridden]
│
└── SportsCar (Inherits from Vehicle)
    └── move() [Overridden]
```

## 🚀 Usage

### Running the Demo

```bash
python oop_demo.py
```

### Creating Your Own Instances

```python
# Create smartphones
phone = Smartphone("Apple", "iPhone 15", 256)
phone.power_on()
phone.make_call("+1234567890")
phone.set_pin_code("0000")

# Create vehicles
my_car = Car("Honda Civic")
tesla = ElectricCar("Tesla Model S")
ferrari = SportsCar("Ferrari 488")

# Demonstrate polymorphism
vehicles = [my_car, tesla, ferrari]
for vehicle in vehicles:
    vehicle.move()  # Each will move differently!
```

## 📊 Examples

### Smartphone Example Output
```
📱 iPhone 15 is booting up... Welcome!
Calling +254700123456...
Battery charged from 100% to 100%.
Installing 'Slack'... Done!
PIN code has been set.
PIN correct. Device unlocked!
```

### Vehicle Example Output
```
Toyota Corolla drives on the road.
Tesla Model 3 glides silently.
Ferrari F8 zooms at high speed!
```

## 🧠 Key Concepts Explained

### Inheritance
- **What**: Child classes inherit attributes and methods from parent classes
- **Example**: `Smartphone` inherits `brand` and `model` from `Device`
- **Benefit**: Code reuse and logical hierarchy

### Polymorphism
- **What**: Same method name, different implementations
- **Example**: `power_on()` works differently for `Device` vs `Smartphone`
- **Benefit**: Flexible and extensible code

### Encapsulation
- **What**: Hiding internal data and controlling access
- **Example**: `_pin_code` is private, accessed only through specific methods
- **Benefit**: Data security and controlled modification

### Method Overriding
- **What**: Child class provides specific implementation of parent method
- **Example**: Each vehicle type has its own `move()` behavior
- **Benefit**: Customized behavior while maintaining common interface

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required

## 📚 Educational Value

This code is perfect for:
- **Students** learning OOP concepts
- **Developers** reviewing OOP principles
- **Instructors** demonstrating practical OOP applications
- **Interview preparation** for OOP-related questions

## 🎓 Learning Outcomes

After studying this code, you'll understand:
- How to design class hierarchies
- When and how to use inheritance
- How polymorphism makes code flexible
- How encapsulation protects data
- Real-world applications of OOP principles

## 🤝 Contributing

Feel free to fork this repository and add more examples or improve existing ones. Some ideas:
- Add more device types (Tablet, Laptop)
- Implement more vehicle features
- Add abstract base classes
- Include composition examples

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Learning! 🎉**

*This demonstration shows that OOP isn't just theory—it's a practical way to organize and structure real-world applications.*