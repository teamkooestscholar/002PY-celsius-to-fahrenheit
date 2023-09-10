# Write a function that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(celcius, conv):
    if conv == "fahrenheit":
        fahrenheit = (celcius * 9/5) + 32
        print("The fahrenheit is ", fahrenheit)
      
    elif conv =="kelvin":
         kelvin = celcius + 273.15
         print("The kelvin is ", kelvin)
        
    else:
        print("Error")

num = float(input("Enter the celcius: "))
ans = input("Enter the conversion(fahrenheit,kelvin) ")

celsius_to_fahrenheit(num,ans)
