#Change Perms
def convert_temperature(temps, scaler):
    if scaler.lower() == 'celsius': #kelvin to celsius
        fahrenheit = (temps * 9/5) + 32
        return fahrenheit
        
    elif scaler.lower() == 'kelvin': #celsius to kelvin
        celsius = temps - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
        
    else:
        raise ValueError("Confirmation Input Incorrect! Try Again.") #error prompt for def main

def main():
    try:
        temps = float(input("Register Desired Value For The Temperature: " )) 
        scaler = input("[Type To 'Kelvin' or 'Celsius' to Confirm Which Conversion You Want]: ")
        
        converted_temperature = convert_temperature(temps, scaler)
        print(f"Converted Values Resulted In {temps} {scaler.capitalize()} is {converted_temperature:.2f} Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e} ")
    
if __name__ == "__main__":
    main()