# Write a function that converts Celsius to Fahrenheit.
def temperature_converter(value, from_scale, to_scale="Celsius"):
    if from_scale == to_scale:
        return value

    if from_scale == "Celsius":
        if to_scale == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_scale == "Kelvin":
            return value + 273.15
    elif from_scale == "Fahrenheit":
        if to_scale == "Celsius":
            return (value - 32) * 5/9
        elif to_scale == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_scale == "Kelvin":
        if to_scale == "Celsius":
            return value - 273.15
        elif to_scale == "Fahrenheit":
            return (value * 9/5) - 459.67

    return "Unsupported temperature scale conversion"

def main():
    try:
        input_temperature = float(input("Enter the temperature value: "))
        input_from_scale = input("Enter the temperature scale to convert from (Celsius/Fahrenheit/Kelvin): ").capitalize()
        input_to_scale = input("Enter the temperature scale to convert to (Celsius/Fahrenheit/Kelvin, default is Celsius): ").capitalize()
        converted_temperature = temperature_converter(input_temperature, input_from_scale, input_to_scale)
        if isinstance(converted_temperature, float):
            print(f"The converted temperature is: {converted_temperature:.2f} {input_to_scale}")
        else:
            print(converted_temperature)
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()

    
