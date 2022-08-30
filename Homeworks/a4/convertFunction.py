# Yelena Baranchuk
# 08/03/2022
# Implement the FR_converter(tf) function. The function does the following:
# converts the Fahrenheit temperature passed as parameter to Réaumur temperature using formula:
# returns the temperature in Réaumur
# In the Python program create a main function which does the following:
# asks the user to enter a temperature in Fahrenheit
# outputs the value given by the user
# calls the function, passing the Fahrenheit value as an argument.
# The function must have one parameter that represents the Fahrenheit temperature. Do not use a global variable.
# prints the value returned by the function.


def main():
    # Get the temperature in Fahrenheit from the user
    temperatureFahrenheit = float(input("Please, input the temperature in Fahrenheit: "))

    # Prin the value given by user
    print("The temperature in Fahrenheit is: ", temperatureFahrenheit)

    # Call the FN_convert function in set the result in the value converterResult
    converterResult = FR_converter(temperatureFahrenheit)

    # Print temperature in Reaumur
    print("The temperature in Reaumur is: ", format(converterResult, '.2f'))
    return


def FR_converter(temperatureFahrenheit):

    # Converts the Fahrenheit temperature passed as parameter to Réaumur temperature using formula:
    temperatureReaumur = (temperatureFahrenheit - 32) * (4 / 9)

    # Return the value temperatureReaumur
    return temperatureReaumur


main()

