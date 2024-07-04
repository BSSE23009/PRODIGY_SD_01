# Function to convert from Celsius to Kelvin and Fahrenheit
def celsiusConversion(value):
    F = (value * 1.8) + 32  # Convert Celsius to Fahrenheit
    K = value + 273.15      # Convert Celsius to Kelvin
    print("Your temperature in Celsius is:", value)
    print("Your temperature in Kelvin is:", K)
    print("Your temperature in Fahrenheit is:", F)

# Function to convert from Kelvin to Celsius and Fahrenheit
def kelvinConversion(value):
    C = value - 273.15      # Convert Kelvin to Celsius
    F = (value - 273.15) * 1.8 + 32  # Convert Kelvin to Fahrenheit
    print("Your temperature in Celsius is:", C)
    print("Your temperature in Kelvin is:", value)
    print("Your temperature in Fahrenheit is:", F)

# Function to convert from Fahrenheit to Celsius and Kelvin
def fahrenheitConversion(value):
    C = (value - 32) * 5/9  # Convert Fahrenheit to Celsius
    K = (value - 32) * 5/9 + 273.15  # Convert Fahrenheit to Kelvin
    print("Your temperature in Celsius is:", C)
    print("Your temperature in Kelvin is:", K)
    print("Your temperature in Fahrenheit is:", value)

# Prompt the user to enter a temperature value
temperatureValue = float(input("Please enter the value of Temperature: "))

# Display the unit selection menu
print("Choose the unit for your value:\n-> press 1 for Kelvin\n-> press 2 for Celsius\n-> press 3 for Fahrenheit")

# Read the user's unit selection
desiredUnit = int(input())

# Perform the appropriate conversion based on the user's selection
if desiredUnit == 1:
    kelvinConversion(temperatureValue)
elif desiredUnit == 2:
    celsiusConversion(temperatureValue)
elif desiredUnit == 3:
    fahrenheitConversion(temperatureValue)
else:
    # Handle invalid unit selection
    print("Invalid unit selection.")
