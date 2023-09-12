#002 Write a function that converts Celsius to Fahrenheit.
def Celsius_to_Fahrenheit(celcius, conv):
    if conv == "Fahrenheit":
        fahrenheit = (celcius * 9/5) + 32
        print("The Fahrenheit is ", fahrenheit)
      
    elif conv =="Kelvin":
         kelvin = celcius + 273.15
         print("The Kelvin is ", kelvin)
        
    else:
        print("ERROR!")

num = float(input("Enter the Celcius: "))
ans = input("Enter the conversion(Fahrenheit, Kelvin) ")

Celsius_to_Fahrenheit(num,ans)
