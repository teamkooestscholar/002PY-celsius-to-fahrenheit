# Write a function that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_temperature(temperature, target_scale):
    if target_scale == "Fahrenheit":
        return celsius_to_fahrenheit(temperature)
    elif target_scale == "Kelvin":
        return celsius_to_kelvin(temperature)
    elif target_scale == "Celsius":
        return temperature
    else:
        return "Please choose from Fahrenheit, Kelvin, or Celsius only."

try:
    temperature = float(input("Enter the temperature: "))
    source_scale = "Celsius"
    
    while True:
        target_scale = input("Enter temperature scale: ")

        converted_temperature = convert_temperature(temperature, target_scale)

        if type(converted_temperature) == float:
            print(f"{temperature} {source_scale} is equal to {converted_temperature:.2f} {target_scale}.")
            break  
        else:
            print(converted_temperature)
except ValueError:
    print("Invalid input, enter a valid temperature value only.")

