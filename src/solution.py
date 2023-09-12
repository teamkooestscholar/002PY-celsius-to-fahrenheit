def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get temperature input from the user
choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")

if choice == 'C' or choice == 'c':
    celsius_temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is {fahrenheit_temperature} degrees Fahrenheit.")
elif choice == 'F' or choice == 'f':
    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature} degrees Celsius.")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
