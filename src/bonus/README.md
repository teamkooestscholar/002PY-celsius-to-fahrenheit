# Temperature Converter with Scale Support

This Python program converts a temperature value between different temperature scales, including Celsius and Kelvin, to degrees Fahrenheit based on user input. It also handles invalid input gracefully.

## Function for Conversion

The code defines a function `temperature_converter` for converting temperatures between different scales. The function takes two parameters: `value`, which is the temperature value, and `scale`, which specifies the input temperature scale ('C' for Celsius or 'K' for Kelvin). It returns the temperature value in degrees Fahrenheit.

```python
def temperature_converter(value, scale):
    """
    Convert temperature from Celsius or Kelvin to Fahrenheit.

    :param value: The temperature value.
    :type value: float
    :param scale: The temperature scale ('C' for Celsius, 'K' for Kelvin).
    :type scale: str
    :return: The temperature value in degrees Fahrenheit.
    :rtype: float
    :raise ValueError: If an invalid temperature scale is provided.
    """
    if scale == 'C':
        # Convert from Celsius to Fahrenheit
        return round((value * 9/5) + 32, 2)
    elif scale == 'K':
        # Convert from Kelvin to Celsius and then to Fahrenheit
        celsius = value - 273.15
        return round((celsius * 9/5) + 32, 2)
    else:
        raise ValueError("Invalid scale. Supported scales: 'C' for Celsius, 'K' for Kelvin")
```

The `temperature_converter` function handles conversions between Celsius and Kelvin and raises a `ValueError` if an unsupported scale is provided.

## User Input and Conversion

The program prompts the user to enter the temperature scale ('C' for Celsius or 'K' for Kelvin) using the `input()` function. It also prompts the user to enter the temperature value in the specified scale as a floating-point number using `float()`.

```python
scale = input("Enter the temperature scale ('C' for Celsius, 'K' for Kelvin): ")
value = float(input(f"Enter the temperature value in {scale}: "))
```

The program then uses the `temperature_converter` function to perform the conversion.

```python
result = temperature_converter(value, scale.upper())
```

## Output

Finally, the program prints the converted temperature value in degrees Fahrenheit with two decimal places.

```python
print(f"{value} degrees {scale} is equal to {result:.2f} degrees Fahrenheit")
```

This program not only accurately converts temperatures between different scales but also handles invalid input by raising a `ValueError` with a helpful error message.
