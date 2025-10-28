def kilometers_to_miles(kilometers):
    return round(kilometers * 0.6213171, 2)


def miles_to_kilometers(miles):
    return round(miles * 1.60934, 2)


def kg_to_pounds(kg):
    return round(kg * 2.20462, 2)


def pounds_to_kg(pounds):
    return round(pounds / 2.20462, 2)


def celsius_to_fahrenheit(celsius):
    return round(((celsius * 9 / 5) + 32), 2)


def fahrenheit_to_celsius(fahrenheit):
    return round(((fahrenheit - 32) * 5 / 9), 2)


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
