# Yelena Baranchuk
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food,
# and then calculate the amount of a 15 percent tip and 7 percent sales tax.
# Display each of these amounts (tip amount and tax amount) and the total.
# Be sure to format your output values as US currency,
# adding the dollar sign and showing 2 places after the decimal (use format(x, '.2f'))

# Get the total charge from the user
chargeForFood = float(input("Please, input total charge for food: "))

# Calculate the tip percent 15%
tipPercent = chargeForFood * 0.15

# Calculate the sales tax 7%
salesTax = chargeForFood * 0.07

# Display formatted total charge
print('The total charge for food is $', format(chargeForFood, ',.2f'), sep='')

# Display formatted tip percents
print('The tip amount is $', format(tipPercent, ',.2f'), sep='')

# Display formatted sales tax
print('The sales tax amount is $', format(salesTax, ',.2f'), sep='')