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
        if choice == "1":
            km_str = input("Enter the number of kilometers: ")
            km = float(km_str)
            miles = kilometers_to_miles(km)
            print(f"Result: {km} km = {miles:.2f} miles")
        elif choice == "2":
            miles_str = input("Enter the number of miles: ")
            miles = float(miles_str)
            km = miles_to_kilometers(miles)
            print(f"Result: {miles} miles = {km:.2f} km")
        elif choice == "3":
            kg_str = input("Enter the number of kilograms: ")
            kg = float(kg_str)
            pounds = kg_to_pounds(kg)
            print(f"Result: {kg} kg = {pounds:.2f} pounds")
        elif choice == "4":
            pounds_str = input("Enter the number of pounds: ")
            pounds = float(pounds_str)
            kg = pounds_to_kg(pounds)
            print(f"Result: {pounds} pounds = {kg:.2f} kg")
        elif choice == "5":
            celsius_str = input("Enter the number of celsius: ")
            celsius = float(celsius_str)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {celsius} celsius = {fahrenheit:.2f} fahrenheit")
        elif choice == "6":
            fahrenheit_str = input("Enter the number of fahrenheit: ")
            fahrenheit = float(fahrenheit_str)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {fahrenheit} fahrenheit = {celsius:.2f} celsius")
        elif choice == "7":
            print("Thank you for using this convertor. Goodbye")
            break
        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    main()
