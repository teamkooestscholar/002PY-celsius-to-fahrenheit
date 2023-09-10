def convert_temperature(value, from_scale, to_scale):
    conversion_formulas = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x * 9/5) - 459.67,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: ((x - 32) * 5/9) + 273.15, 
        }
        
    if (from_scale, to_scale) in conversion_formulas:
        conversion_func = conversion_formulas[(from_scale, to_scale)]
        result = conversion_func(value)
        return result
    return None
    
value = float(input("Please enter the desired temperature: "))
from_scale = input("Please enter the temperature you want to convert (Celsius, Fahrenheit, Kelvin): ").strip()
to_scale = input("Please enter the temperature your converting to (Celsius, Fahrenheit, Kelvin): ").strip()

result = convert_temperature(value, from_scale, to_scale)

if result is not None:
    print(f"{value} degrees {from_scale} is {result:.2f} degrees {to_scale}")
else:
    print("The Temperature you entered is invalid.")
