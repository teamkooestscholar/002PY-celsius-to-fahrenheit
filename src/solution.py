def celsius_to_fahrenheit(celsius, conversion):
    if conversion == "fahrenheit":
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    elif conversion == "kelvin":
        kelvin = celsius + 273.15
        return kelvin
    else:
        return "Error: Invalid conversion type"

celsius = float(input("Enter the Celsius temperature: "))
conversion_type = input("Enter the conversion type (fahrenheit or kelvin): ")

result = celsius_to_fahrenheit(celsius, conversion_type)
if isinstance(result, str):
    print(result)
else:
    print("The", conversion_type, "is", result)
