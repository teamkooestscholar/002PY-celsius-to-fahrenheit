def convert_temperature(value, from_scale, to_scale="Celsius"):
    if from_scale == "Celsius" and to_scale == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_scale == "Celsius" and to_scale == "Kelvin":
        return value + 273.15
    elif from_scale == "Fahrenheit" and to_scale == "Celsius":
        return (value - 32) * 5/9
    elif from_scale == "Fahrenheit" and to_scale == "Kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_scale == "Kelvin" and to_scale == "Celsius":
        return value - 273.15
    elif from_scale == "Kelvin" and to_scale == "Fahrenheit":
        return ((value - 273.15) * 9/5) + 32
    else:
        raise ValueError("Invalid temperature scale. Supported scales are 'Celsius', 'Fahrenheit', and 'Kelvin'.")

def main():
    try:
        value = float(input("Enter the temperature value: "))
        from_scale = input("Enter the source temperature scale (Celsius, Fahrenheit, or Kelvin): ").capitalize()
        to_scale = input("Enter the target temperature scale (Celsius, Fahrenheit, or Kelvin): ").capitalize()
        
        result = convert_temperature(value, from_scale, to_scale)
        
        print(f"{value} {from_scale} is equal to {result} {to_scale}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric temperature value and valid temperature scales.")

if __name__ == "__main__":
    main()
