# Yelena Baranchuk
# Program 2

# Get the temperature in Fahrenheit from the user
temperatureInFahrenheit = int(input('Input temperature in Fahrenheit, please: '))

# Calculate the temperature in kelvin using the formula
temperatureInKelvin = (temperatureInFahrenheit + 459.67) * (5/9)

# Print the temperature in Kelvin. To concatenate string and integer or float, we have to convert int in str.
print("The temperature in Kelvin is: " + str(temperatureInKelvin))