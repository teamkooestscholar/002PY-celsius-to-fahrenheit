def celsius_to_fahrenheit(value, target_scale):
    if target_scale.lower() == 'fahrenheit':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif target_scale.lower() == 'kelvin':
        kelvin = value + 273.15
        return kelvin
    else:
        return "Unsupported target scale. Please specify 'Fahrenheit' or 'Kelvin'."

if __name__ == "__main__":
    temperature_celsius = float(input("Enter temperature in Celsius: "))
    target_scale = input("Enter the target temperature scale (Fahrenheit/Kelvin): ")

    result = celsius_to_fahrenheit(temperature_celsius, target_scale)

    if isinstance(result, (float, int)):
        print(f"{temperature_celsius}°C is {result}°{target_scale}.")
    else:
        print(result)