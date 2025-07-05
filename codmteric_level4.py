def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

conversion_map = {
    '1': ('Temperature', celsius_to_fahrenheit, 'Celsius', 'Fahrenheit'),
    '2': ('Distance', km_to_miles, 'Kilometers', 'Miles'),
    '3': ('Weight', kg_to_pounds, 'Kilograms', 'Pounds')
}

while True:
    print("\nUnit Converter:")
    for key, value in conversion_map.items():
        print(f"{key}. {value[0]} ({value[2]} ➜ {value[3]})")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == '4':
        print("Exiting... Bye!")
        break

    if choice in conversion_map:
        try:
            amount = float(input(f"Enter value in {conversion_map[choice][2]}: "))
            result = conversion_map[choice][1](amount)
            print(f"{amount:.2f} {conversion_map[choice][2]} = {result:.2f} {conversion_map[choice][3]}")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    else:
        print("Invalid choice. Try again.")