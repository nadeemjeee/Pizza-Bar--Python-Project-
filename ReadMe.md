# 🍕  Pizza Bar - CLI Project

## Content
- Explains **what** the program does  
- Describes **how to install dependencies**  
- Explains **how to run tests**  
- Ends with a **short logbook/reflection**
## Description
This is a Python project where you build a Command Line Interface (CLI) application for ordering pizzas.  
The user can place new orders, choose sizes and extra toppings, and view previously saved orders.  
All data is stored in a JSON file (db.json).

## Installation

### Step 1: Create a Virtual Environment (venv)
A virtual environment helps you isolate your project dependencies from other Python projects.

# Create a new virtual environment
```bash
python3 -m venv venv
```
# Activate the virtual environment
# On macOS/Linux:
```bash
source venv/bin/activate
```
### Disable virtual environment
```bash
deactivate
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install: pytest – for testing
(No other dependencies are required for this CLI app)

# requirements.txt
pytest

### When you run the program, you will see:
Welcome to Python Pizza Bar
1. Place a new order
2. Show previous order
3. Quit
You can then follow the on-screen instructions to place a new pizza order or view saved ones.

### How to Run application/PIZZA BAR (PYTHON PROJECT)
## For macOS / Linux users
```bash
source venv/bin/activate
python3 app/main.py
```
## For Windows users
```bash
venv\Scripts\activate
python app/main.py
```

### How to Run Tests
```bash
pytest
```

### When you are done working, you can deactivate the virtual environment
deactivate

### Logbook / Reflection

What was difficult:
Connecting all modules (main program, logic, and file handling) and managing invalid user inputs.
How it was solved:
I separated the logic into different files:
    pizza_order.py for classes and price calculation
    storage_service.py for reading/writing JSON data
    and used try/except for error handling.

What I learned:
How to design a structured Python CLI application
How to handle user input and validation
How to save and load data using JSON
How to write and run automated tests with pytest
**************
