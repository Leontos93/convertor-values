# Simple Unit Converter in Python

This project is a simple, command-line unit converter written in Python. It's designed as a learning exercise to demonstrate fundamental programming concepts, including functions, user input, conditional logic, and data structures.

The converter can perform the following conversions:
*   Kilometers to Miles
*   Miles to Kilometers
*   Kilograms to Pounds
*   Pounds to Kilograms
*   Celsius to Fahrenheit
*   Fahrenheit to Celsius

The project includes two different implementations to showcase two common approaches to building menu-driven applications.

## Two Versions Included

This repository contains two Python files, each implementing the converter with a different logical structure.

### 1. `converter_if.py` - The Simple `if-elif-else` Approach

This version uses a straightforward `if-elif-else` control structure to handle the user's menu choice.

*   **How it works:** The program displays a menu and uses a chain of `if/elif` statements to check the user's input. Each block of code is responsible for handling one specific conversion.
*   **Pros:** Very easy to read and understand for beginners, as the logic for each menu choice is explicitly written out.
*   **Cons:** Adding new conversions is tedious. It requires adding a new `elif` block and can lead to repetitive code, violating the DRY (Don't Repeat Yourself) principle.

### 2. `converter_dict.py` - The Advanced Dictionary-Driven Approach

This version uses a Python dictionary to manage all the conversion options in a more scalable and organized way.

*   **How it works:** A dictionary stores all the information related to each conversion (the description, the function to call, and the unit names). The main loop becomes generic, simply looking up the user's choice in the dictionary and executing the corresponding logic.
*   **Pros:**
    *   **Scalable:** To add a new conversion, you only need to add one new entry to the dictionary. The main loop logic doesn't need to be changed.
    *   **DRY (Don't Repeat Yourself):** It avoids code duplication by using a single, generic block of code to handle user input and display results.
    *   **Organized:** All conversion data is neatly organized in one central data structure.

## How to Run

Make sure you have Python 3 installed on your system.

1.  Clone or download the repository.
2.  Open your terminal or command prompt and navigate to the project directory.
3.  Choose which version you want to run:

To run the simple version:
```bash
python converter_if.py
```

To run the advanced, dictionary-driven version:
```bash
python converter_dict.py
```

You will then be prompted to make a selection from the menu.