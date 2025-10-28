def kilometers_to_miles(kilometers):
    return kilometers * 0.6213171


def miles_to_kilometers(miles):
    return miles * 1.60934, 2


def kg_to_pounds(kg):
    return kg * 2.20462, 2


def pounds_to_kg(pounds):
    return pounds / 2.20462, 2


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        print("\n--- Converter Menu ---")
        print("--- Length ---")
        print("1: Kilometers -> Miles")
        print("2: Miles -> Kilometers")
        print("--- Weight ---")
        print("3: Kilograms -> Pounds")
        print("4: Pounds -> Kilograms")
        print("---Temperature---")
        print("5: Celsius -> Fahrenheit")
        print("6: Fahrenheit -> Celsius")
        print("7: Exit")

        choice = input("Make your choice: ")
