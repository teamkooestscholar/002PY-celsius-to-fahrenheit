def convert_temperature(temperature, scale):
    if scale == "Celsius":
        return (temperature * 9/5) + 32
    elif scale == "Kelvin":
        return (temperature - 273.15) * 9/5 + 32
    else:
        return "Unsupported scale. Supported scales: Celsius, Kelvin"

# Command-line tool
def main():
    try:
        temperature = float(input("Enter the temperature: "))
        scale = input("Enter the temperature scale (Celsius/Kelvin): ").capitalize()

        converted_temperature = convert_temperature(temperature, scale)
        if type(converted_temperature) == float:
            print(f"{temperature} {scale} is equal to {converted_temperature} Fahrenheit.")
        else:
            print(converted_temperature)

    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()