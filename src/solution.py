def convert_temperature(celsius, target_scale):
    if target_scale == "fahrenheit":
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    elif target_scale == "kelvin":
        kelvin = celsius + 273.15
        return kelvin
    else:
        return "Invalid target temperature scale"

temperature_celsius = float(input("Enter the temperature in Celsius: "))

temperature_fahrenheit = convert_temperature(temperature_celsius, "fahrenheit")
print("Temperature in Fahrenheit:", temperature_fahrenheit)

temperature_kelvin = convert_temperature(temperature_celsius, "kelvin")
print("Temperature in Kelvin:", temperature_kelvin)