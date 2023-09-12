# Write a function that converts Celsius to Fahrenheit.

def temperature_converter(value, scale):
    if scale == 'C':
        # Convert from Celsius to Fahrenheit
        return round((value * 9/5) + 32, 2)
    elif scale == 'K':
        # Convert from Kelvin to Celsius and then to Fahrenheit
        celsius = value - 273.15
        return round((celsius * 9/5) + 32, 2)
    else:
        raise ValueError("Invalid scale. Supported scales: 'C' for Celsius, 'K' for Kelvin")

try:
    scale = input("Enter the temperature scale ('C' for Celsius, 'K' for Kelvin): ")
    value = float(input(f"Enter the temperature value in {scale}: "))
    result = temperature_converter(value, scale.upper())
    print(f"{value} degrees {scale} is equal to {result:.2f} degrees Fahrenheit")
except ValueError as e:
    print(e)