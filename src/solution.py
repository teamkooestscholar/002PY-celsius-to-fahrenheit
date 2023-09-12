def convert_temperature(value, scale='Celsius'):
    if scale == 'C':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif scale == 'K':
        fahrenheit = (value - 273.15) * 9/5 + 32
        return fahrenheit
    else:
        return "Invalid temp. scale"

if __name__ == "__main__":
    temperature = float(input("Enter temp. value: "))
    scale = input("Enter the temp. scale (C/K): ").strip()

    result = convert_temperature(temperature, scale)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"{temperature} {scale} is approximately {result} Fahrenheit")