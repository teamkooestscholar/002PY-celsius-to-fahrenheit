def convert_temperature(value, from_scale, to_scale):
    if from_scale == 'C' and to_scale == 'F':
        return (value * 9/5) + 32
    elif from_scale == 'F' and to_scale == 'C':
        return (value - 32) * 5/9
    else:
        return value  
        
if __name__ == "__main__":
    try:
        value = float(input("Enter temperature: "))
        from_scale = input("Enter temperature scale [C for Celsius, F for Fahrenheit]: ").upper()
        to_scale = input("Enter target temperature scale [C for Celsius, F for Fahrenheit]: ").upper()

        converted_value = convert_temperature(value, from_scale, to_scale)
        print(f"The converted temperature is: {converted_value} {to_scale}")
    except ValueError:
        print("Invalid input enter a valid numeric temperature value.")
