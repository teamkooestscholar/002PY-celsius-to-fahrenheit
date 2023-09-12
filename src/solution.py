# Write a function that converts Celsius to Fahrenheit.
#Canane, Jewel Mae P.

def convert(temp, scale):
    if scale == 'C':
        return (temp * 9/5) + 32
    elif scale == 'K':
        c_temp = temp - 273.15
        return (c_temp * 9/5) + 32
    else:
        return "Invalid scale. Please enter 'C' for Celsius or 'K' for Kelvin."

scale = input("Enter which temperature scale ('C' for Celsius, 'K' for Kelvin): ").upper()
temp = float(input("Enter the temperature value: "))

converted = convert(temp, scale)
    
if isinstance(converted, float):
    print(f"{temp}{scale} is roughly {converted:.2f} Fahrenheit.")
else:
    print(converted)