# Yelena Baranchuk


# Get the information about package's weight

weight = float(input('Please, input the weight of the package: '))

# weight of package 2 or less
if weight <= 2:
    # Calculate the shipping charges
    shippingCharges = weight * 1.10
    # Print the total charges for the package
    # Rounds to two decimal places
    print('Total charges for your package is: ',  round(shippingCharges, 2))
elif 2 < weight <= 6:
    # Calculate the shipping charges
    shippingCharges = weight * 2.20
    # Print the total charges for the package
    # Rounds to two decimal places
    print('Total charges for your package is: ', round(shippingCharges, 2))
elif  6 < weight <= 10:
    # Calculate the shipping charges
    shippingCharges = weight * 3.70
    # Print the total charges for the package
    # Rounds to two decimal places
    print('Total charges for your package is: ', round(shippingCharges, 2))
else:
    # Calculate the shipping charges
    shippingCharges = weight * 3.80
    # Print the total charges for the package
    # Rounds to two decimal places
    print('Total charges for your package is: ', round(shippingCharges, 2))





