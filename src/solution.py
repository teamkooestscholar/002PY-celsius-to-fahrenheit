def temperature_converter(temperature, target_scale='F'):
    """
    Convert a temperature from one scale to another.

    Args:
        temperature (float): The temperature value to convert.
        target_scale (str): The target temperature scale (default is 'F').

    Returns:
        float: The converted temperature.
    """
    if target_scale == 'F':
        return (temperature * 9/5) + 32
    elif target_scale == 'K':
        return temperature + 273.15
    else:
        raise ValueError("Invalid target scale. Supported scales: 'F', 'K'.")

if __name__ == "__main__":
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        target_scale = input("Enter the target scale (F/K): ").capitalize()

        if target_scale not in ['F', 'K']:
            raise ValueError("Invalid target scale.  'F', 'K'. only")

        converted_temperature = temperature_converter(celsius, target_scale)
        print(f"The temperature in {target_scale} is: {converted_temperature}")
    except ValueError as e:
        print(f"Error: {e}")
        
#Enter the temperature in Celsius: 3
#Enter the target scale (F/K): r
#ERROR!
#Error: Invalid target scale.  'F', 'K'. only

#Enter the temperature in Celsius: 4
#Enter the target scale (F/K): f
#The temperature in F is: 39.2

#Enter the temperature in Celsius: 5
#Enter the target scale (F/K): k
#The temperature in K is: 278.15