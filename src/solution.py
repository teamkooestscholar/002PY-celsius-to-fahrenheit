def temperature_converter(temperature, from_scale="Celsius", to_scale="Fahrenheit"):
    if from_scale == to_scale:
        return temperature

    if from_scale == "Celsius":
        if to_scale == "Fahrenheit":
            return (temperature * 9/5) + 32
        elif to_scale == "Kelvin":
            return temperature + 273.15
    elif from_scale == "Kelvin":
        if to_scale == "Celsius":
            return temperature - 273.15
        elif to_scale == "Fahrenheit":
            return (temperature - 273.15) * 9/5 + 32
    elif from_scale == "Fahrenheit":
        if to_scale == "Celsius":
            return (temperature - 32) * 5/9
        elif to_scale == "Kelvin":
            return (temperature - 32) * 5/9 + 273.15

    raise ValueError("Invalid input or output temperature scale")

celsius_temp = 25
fahrenheit_temp = temperature_converter(celsius_temp, from_scale="Celsius", to_scale="Fahrenheit")
print(f"{celsius_temp} degrees Celsius is {fahrenheit_temp} degrees Fahrenheit")

# Bonus Challenge
def main():
    input_temp = float(input("Enter the temperature value: "))
    from_scale = input("Enter the input temperature scale (e.g., Celsius, Kelvin, Fahrenheit): ")
    to_scale = input("Enter the desired output temperature scale (e.g., Celsius, Kelvin, Fahrenheit): ")

    try:
        converted_temp = temperature_converter(input_temp, from_scale, to_scale)
        print(f"{input_temp} degrees {from_scale} is {converted_temp} degrees {to_scale}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()