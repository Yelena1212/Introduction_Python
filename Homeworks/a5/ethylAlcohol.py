# Yelena Baranchuk
# Ethyl Alcohol
# The freezing point of Ethyl Alcohol is -173
# and the boiling point is 172,
# write a program to request the ethyl alcohol temperature (Fahrenheit)
# from user then display whether the temperature is
# at or below freezing, at or above boiling, or somewhere in-between.

# Get the temperature in Fahrenheit from the user
temperatureFahrenheit = float(input("Please, input the temperature of Ethyl Alcohol in Fahrenheit: "))

# Display the temperature inputted by the user
print("The temperature in Fahrenheit is: ", temperatureFahrenheit)

# The temperature at -173 is freezing Ethyl Alcohol
if temperatureFahrenheit == -173:
    # Display the temperature is freezing of Ethyl Alcohol
    print(f"The {temperatureFahrenheit} is the temperature of freezing of Ethyl Alcohol")

# The temperature below -173 is below freezing Ethyl Alcohol
elif temperatureFahrenheit < -173:
    # Display the temperature is below freezing of Ethyl Alcohol
    print(f"The {temperatureFahrenheit} is the temperature of below freezing of Ethyl Alcohol")

# The temperature at 172 is boiling Ethyl Alcohol
elif temperatureFahrenheit == 172:
    # Display the temperature is boiling of Ethyl Alcohol
    print(f"The {temperatureFahrenheit} is the temperature of boiling of Ethyl Alcohol")

# The temperature above -173 is above boiling Ethyl Alcohol
elif temperatureFahrenheit > 172:
    # Display the temperature is above boiling of Ethyl Alcohol
    print(f"The {temperatureFahrenheit} is the temperature of above boiling of Ethyl Alcohol")
else:
    # Display the temperature is somewhere in between boiling and freezing of Ethyl Alcohol
    print(f"The {temperatureFahrenheit} is the temperature of somewhere in-between freezing and boiling of Ethyl Alcohol")


