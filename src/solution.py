# Define a function for converting Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    print("Celsius to Fahrenheit Converter")

    try:
        # Prompt the user for a temperature in Celsius and convert it to Fahrenheit.
        celsius = float(input("Please enter a temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)

        # Display the converted temperature with two decimal places.
        print(f"{celsius:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit.")
    except ValueError:
        print("Invalid input. Please provide a valid temperature in Celsius.")

if __name__ == "__main__":
    main()