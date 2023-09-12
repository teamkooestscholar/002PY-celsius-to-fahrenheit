# Write a function that converts Celsius to Fahrenheit.
def convert_cel_to_far(c):
    """ converts celsius to Fahrenheit """
    f = c * 9/5 + 32
    return f


def convert_far_to_cel(f):
    """ converts fahrenheit to celsius """
    c = (f - 32) * 5/9
    return c


user_cel = float(input("Enter a temperature in degrees F: "))
print(f"{user_cel} degrees F = {convert_far_to_cel(user_cel):.2f} degrees C")

user_far = float(input("Enter a temperature in degrees C: "))
print(f"{user_far} degrees C = {convert_cel_to_far(user_far):.2f} degrees F")
