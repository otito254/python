Device & Smartphone OOP Demo
Overview
This project is a Python demonstration of Object-Oriented Programming (OOP) concepts:

Inheritance (child class extending a parent class)

Polymorphism (overriding methods to change behavior)

Encapsulation (private attributes and controlled access methods)

It models a generic Device and a more specific Smartphone with realistic actions like making calls, charging the battery, and installing apps.

Features
🔹 Classes & OOP Concepts
Device (Parent Class)

Attributes: brand, model

Method: power_on() — generic startup message

Smartphone (Child Class)

Inherits from Device

Extra attributes: storage_gb, battery_level (default 100%)

Overridden power_on() — custom startup with emoji (polymorphism)

Methods:

make_call(number) — simulate making a phone call

charge(percent) — increase battery level without exceeding 100%

install_app(app_name) — simulate installing an app

Encapsulation Example: private attribute _pin_code with:

set_pin_code(pin) — set a security PIN

unlock(pin) — validate PIN before unlocking

Installation & Requirements
Python 3.7+ recommended

No external libraries required — runs with Python’s standard library

How to Run
Clone or download this repository.

Open a terminal in the project directory.

Run:

bash
python device_demo.py
(Replace device_demo.py with your actual filename)

Example Output
Code
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
File Structure
Code
.
├── device_demo.py   # Main Python program
└── README.md        # Project documentation (this file)
Learning Outcomes
By reviewing or extending this code, you will:

Understand class construction and attribute initialization

Practice inheritance and super() calls

Apply method overriding for polymorphic behavior

Explore encapsulation via private attributes and controlled access

Learn clean, readable Python coding style with docstrings and comments

Possible Extensions
Add more device types (e.g., Tablet, Laptop) inheriting from Device

Store installed apps in a list and display them

Add battery consumption when making calls or installing apps

Implement a lock state that blocks actions until unlocked