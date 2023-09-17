# Write a function that converts Celsius to Fahrenheit.
def convert_temperature(temperature, scale):
    if scale.lower() == 'celsius':
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif scale.lower() == 'kelvin':
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    else:
        raise ValueError("Unsupported temperature scale")

def main():
    try:
        temperature = float(160) #input here
        scale = input('celsius') #'celsius'/'kelvin'
        
        converted_temperature = convert_temperature(temperature, scale)
        print(f"{temperature} {scale.capitalize()} is {converted_temperature:.2f} Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()

#edit