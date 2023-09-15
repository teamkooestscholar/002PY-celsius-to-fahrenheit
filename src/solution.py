# Write a function that converts Celsius to Fahrenheit.
def convert_temperature(celsius, target_scale):
    if target_scale == "C":
        return celsius
    elif target_scale == "F":
        return (celsius * 9 / 5) + 32
    elif target_scale == "K":
        return celsius + 273.15
    else:
        raise ValueError("Invalid input.")

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        target_scale = input("Enter the target temperature scale (C, F, or K): ").upper()

        if target_scale not in ["C", "F", "K"]:
            print("Invalid target temperature scale. Please enter C, F, or K.")
            return

        converted_temperature = convert_temperature(celsius, target_scale)
        print(f"{celsius} degrees Celsius is equal to {converted_temperature} degrees {target_scale}.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
    