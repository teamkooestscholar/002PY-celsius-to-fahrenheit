def convert_temperature(temperature, from_unit):
    if from_unit.lower() == 'celsius':
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif from_unit.lower() == 'kelvin':
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    else:
        raise ValueError("Unsupported temperature unit")

def main():
    try:
        input_temperature = float(input("Enter temperature: "))
        input_unit = input("Enter current temperature unit (celsius/kelvin): ")
        
        converted_temperature = convert_temperature(input_temperature, input_unit)
        target_unit = 'Fahrenheit'
        print(f"{input_temperature} {input_unit.capitalize()} is {converted_temperature:.2f} {target_unit}.")
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()



# added co author 