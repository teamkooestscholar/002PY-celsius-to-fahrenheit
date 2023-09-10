def convert_temperature(value, scale='Celsius'):
    if scale == 'Celsius':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif scale == 'Kelvin':
        fahrenheit = (value - 273.15) * 9/5 + 32
        return fahrenheit
    else:
        return "Invalid scale. Supported scales are 'Celsius' and 'Kelvin'."

def main():
    try:
        temperature = float(input("Enter the temperature value: "))
        scale = input("Enter the temperature scale (Celsius or Kelvin): ").capitalize()

        result = convert_temperature(temperature, scale)
        if type(result) == float:
            print(f"{temperature} {scale} is {result} Fahrenheit.")
        else:
            print(result)
    except ValueError:
        print("Invalid input. Please enter a valid numerical temperature value.")

if __name__ == "__main__":
    main()
