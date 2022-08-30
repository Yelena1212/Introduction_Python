# Yelena Baranchuk
# 08/06/2022
# Implement the coneVolume( height, radius )
# function that calculates and displays the volume of a cone with the given height and base radius.
# in the main function, write the code that:
# asks for height and base radius of the cone,
# calls the function, passing to it the height and radius values as arguments.
# and prints the volume to the console.

import math

def main():
# Get the height of cone from the user
    heightOfCone = int(input("Please, input the height of the cone: "))

# Get the base radius of the cone from the user
    radiusOfCone = int(input("Please, input the base radius of the cone: "))

# Call the volume_of_cone function
    calculatedVolumeCone = volume_of_cone(heightOfCone, radiusOfCone)

# Print to console the volume of the cone with given height and base radius
    print("The height of the cone is: ", heightOfCone)
    print("The base radius of the cone is: ", radiusOfCone)
    print("The volume of the cone is: ", format(calculatedVolumeCone, '.2f'))
    return


def volume_of_cone(heightOfCone, radiusOfCone):
    # area = 1/3 * PI * radius * height
    # Calculate the volume of the cone
    volumeOfCone = (1 / 3) * (math.pi * radiusOfCone ** 2 * heightOfCone)

    # return the volume of the cone
    return volumeOfCone

main()