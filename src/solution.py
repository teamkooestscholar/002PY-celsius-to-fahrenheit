# Write a function that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(temp, scale):
    
    if scale == "fahrenheit":
        fahrenheit = (temp * 9/5) + 32
        print("The fahrenheit is ", fahrenheit)
      
    elif scale =="kelvin":
         kelvin = temp + 273.15
         print("The kelvin is ", kelvin)
    else:
        print("Invalid scale: " + scale)
    
num = float(input("Enter the Temperature in Celsius: "))
conversion = input("Enter the conversion(fahrenheit,kelvin) ")

celsius_to_fahrenheit(num,conversion)
