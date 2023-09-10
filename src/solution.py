def convert_temperature(value, scale='Celsius'):
    if scale == 'Celsius':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif scale == 'Kelvin':
        fahrenheit = (value - 273.15) * 9/5 + 32
        return fahrenheit
    else:
        return "Unsupported temperature scale"

if __name__ == "__main__":
    temperature = float(input("Enter a temperature value: "))
    scale = input("Enter the temperature scale (Celsius/Kelvin): ").strip()

    result = convert_temperature(temperature, scale)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"{temperature} {scale} is approximately {result} Fahrenheit")