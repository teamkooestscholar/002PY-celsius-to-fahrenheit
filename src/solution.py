# # Write a function that converts Celsius to Fahrenheit.
# def celsius_to_fahrenheit(_):
#     pass

def convert_temperature(temperature, scale):
    if scale == "Celsius":
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif scale == "Kelvin":
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    else:
        return "Unsupported temperature scale"

if __name__ == "__main__":
    temperature = float(input("Enter the temperature: "))
    scale = input("Enter the temperature scale (Celsius or Kelvin): ").capitalize()

    converted_temperature = convert_temperature(temperature, scale)

    if isinstance(converted_temperature, float):
        print(f"{temperature} {scale} is equal to {converted_temperature:.2f} Fahrenheit.")
    else:
        print(converted_temperature)
