def kilometers_to_miles(val):
    return val * 0.6213171


def miles_to_kilometers(val):
    return val * 1.60934


def kg_to_pounds(val):
    return val * 2.20462


def pounds_to_kg(val):
    return val / 2.20462


def celsius_to_fahrenheit(val):
    return (val * 9 / 5) + 32


def fahrenheit_to_celsius(val):
    return (val - 32) * 5 / 9


def main():
    conversions = {
        "1": ("Kilometers -> Miles", kilometers_to_miles, "km", "miles"),
        "2": ("Miles -> Kilometers", miles_to_kilometers, "miles", "km"),
        "3": ("Kilograms -> Pounds", kg_to_pounds, "kg", "pounds"),
        "4": ("Pounds -> Kilograms", pounds_to_kg, "pounds", "kg"),
        "5": ("Celsius -> Fahrenheit", celsius_to_fahrenheit, "celsius", "fahrenheit"),
        "6": ("Fahrenheit -> Celsius", fahrenheit_to_celsius, "fahrenheit", "celsius"),
    }

    while True:
        print("\n--- Converter Menu ---")
        for key, value in conversions.items():
            print(f"{key}: {value[0]}")
        print(f"{len(conversions) + 1}: Exit")
        choice = input("Make your choice: ")
        if choice in conversions:
            description, func, from_unit, to_unit = conversions[choice]
            val_str = input(f"Enter the value in '{from_unit}': ")
            value = float(val_str)
            result = func(value)
            print(f"Result: {value} {from_unit} = {result:.2f} {to_unit}")
        elif choice == str(len(conversions) + 1):
            print("Thank you for using the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
