#function to convert celsius/kelvin to fahrenheit

def celsius_to_fahrenheit(value, scale):
    if scale == 'celsius':
        celfah = round((value * (9/5) + 32), 2)
        return f"{value} Celcius = {celfah} Fahrenheit"
    elif scale == 'kelvin':
        kelfah = round((value - 273.15) * (9/5) + 32, 2)
        return f"{value} Kelvin = {kelfah} Fahrenheit"
    else:
        return "Wrong input choice"
        
user_scale = input("Which do you want to convert to fahrenheit? celsius or kelvin?: ").lower()
user_value = float(input("Enter a value: "))

print(celsius_to_fahrenheit(user_value, user_scale))