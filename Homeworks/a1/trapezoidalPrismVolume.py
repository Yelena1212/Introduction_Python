# Yelena Baranchuk
# Program 3


# Get the length of trapezoidal prisms
length = int(input("Input Length of trapezoidal prisms: "))

# Get the height of trapezoidal prisms
height = int(input("Input Height of trapezoidal prisms: "))

# Get the base width of trapezoidal prisms
baseWidth = int(input("Input Base Width of trapezoidal prisms: "))

# Get the top width of trapezoidal prisms
topWidth = int(input("Input Top Width of trapezoidal prisms: "))

# Set all inputted information in the formula of trapezoidal prisms
volumeOfTrapezoidalPrisms = length * height * ((baseWidth + topWidth) / 2)

# Print the result converted in the string
print("The volume of the trapezoidal prisms is: " + str(volumeOfTrapezoidalPrisms))

# Get reduce all volumes (length, height, top width and base width)
# Print reduced length
reducedLength = length * 0.75
print(reducedLength)
# Print reduced height
reducedHeight = height * 0.75
print(reducedHeight)
# Print reduced base width
reducedBaseWidth = baseWidth * 0.75
print(reducedBaseWidth)
# Print reduced top width
reducesTopWidth = topWidth * 0.75
print(reducesTopWidth)

# Calculate the volume of the trapezoidal prisms via formula
reducedVolumeOfTrapezoidalPrisms = reducedLength * reducedHeight * ((reducedBaseWidth + reducesTopWidth) / 2)

# Print reduced volume of the trapezoidal prisms to the console
print("The volume of the trapezoidal prisms with reduced measurements of the prism by 25%: " + str(reducedVolumeOfTrapezoidalPrisms))
