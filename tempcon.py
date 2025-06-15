def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {f:.2f}°F and {k:.2f}K")
    elif unit.lower() == 'fahrenheit':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {c:.2f}°C and {k:.2f}K")
    elif unit.lower() == 'kelvin':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"{value}K is equal to {c:.2f}°C and {f:.2f}°F")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

# User input
try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
    convert_temperature(temp, unit)
except ValueError:
    print("Please enter a valid numerical temperature value.")
