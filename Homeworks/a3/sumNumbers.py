# Yelena Baranchuk
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.
# Do not use input validation in this program -- it does not apply.

#Declare the sum and numbers variables
sum = 0
number = 1
# Start while loop
while number > 0:
    # Get the number from the user
    number = int(input('Enter a positive number: '))
    #Check if number more than 0 add the number to the sum
    if number > 0:
        sum += number
        # print the sum of the numbers if user input negative number, if positive, continue while loop
print("The sum of the numbers is", sum)