def convert_temp(val, from_scale, to_scale):
    if from_scale == to_scale:
        return val

    if from_scale == 'C':
        if to_scale == 'F':
            return (val * 9/5) + 32
        elif to_scale == 'K':
            return val + 273.15
    elif from_scale == 'F':
        if to_scale == 'C':
            return (val - 32) * 5/9
        elif to_scale == 'K':
            return ((val - 32) * 5/9) + 273.15
    elif from_scale == 'K':
        if to_scale == 'C':
            return val - 273.15
        elif to_scale == 'F':
            return ((val - 273.15) * 9/5) + 32
    
    raise ValueError("Invalid temperature scales.")

def main():
    print("Temperature Converter")
    try:
        val = float(input("Enter temperature value: "))
        from_s = input("Enter input scale (C/K/F): ").upper()
        to_s = input("Enter output scale (C/K/F): ").upper()

        converted_val = convert_temp(val, from_s, to_s)
        print(f"{val}{from_s} is {converted_val}{to_s}")
    except ValueError as e:
        print(f"Error: {e}. Please provide valid input.")

if __name__ == "__main__":
    main()
