# Convert Celsius to Fahrenheit

This Python program converts a temperature value in degrees Celsius to degrees Fahrenheit based on user input.

## Function for Conversion

The code defines a function `celsius_to_fahrenheit` for converting degrees Celsius to degrees Fahrenheit. It uses the formula `(celsius * 9/5) + 32` for the conversion.

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    :param celsius: The temperature in degrees Celsius.
    :type celsius: float
    :return: The temperature in degrees Fahrenheit.
    :rtype: float
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```

The `celsius_to_fahrenheit` function takes the temperature in degrees Celsius as input and returns the equivalent temperature in degrees Fahrenheit.

## User Input and Conversion

The program prompts the user to enter the desired temperature in degrees Celsius using the `input()` function. It then converts the user input to a floating-point number using `float()`.

```python
celsius = float(input("Enter the desired temperature in degrees Celsius: "))
```

After obtaining the temperature in Celsius from the user, the program uses the `celsius_to_fahrenheit` function to perform the conversion.

```python
fahrenheit = celsius_to_fahrenheit(celsius)
```

## Output

Finally, the program prints the converted temperature in degrees Fahrenheit along with the original temperature in degrees Celsius.

```python
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
```

This program accurately converts temperatures from Celsius to Fahrenheit based on the user's input.
