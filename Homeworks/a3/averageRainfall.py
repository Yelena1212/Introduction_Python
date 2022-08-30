# Yelena Baranchuk
# assignment 3

# Write a program that uses 2 nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. Be sure to validate the input to be positive.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# To simplify this loop, you don't need to validate the rainfall value.
# After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
# Here is a snapshot on how a run should look: (You must "duplicate the prompt message" as it is shown when your program is run)
# NOTE-> I SUGGEST THAT WHEN YOU TEST YOUR PROGRAM, YOU DO 2 YEARS (24 MONTHS)
# BUT DON'T HARDCODE THE OUTER LOOP TO BE FOR 2 YEARS AS THE PROGRAM SHOULD ACCOMOMODATE ANY NUMBER OF YEARS WE MIGHT WANT TO RUN THE CODE FOR
# As you can see from the example output, they just show the running of the code for 1 year

#Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall, the number
# of years, and the total number of months.
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0


# Get number of years
years = int(input('Enter the number of years: '))

# Add to total number of months
totalMonths = 12 * years

# Make sure that number of year is positive
if years < 0:
    print('Invalid: ', int(input('Enter a positive number: ')))
else:
# Get rainfall by month
    for year in range(years):
        print('For year ', year + 1, ':')
        for month in range(12):
            print('Enter the rainfall for year ', year + 1, ',', 'month', month + 1, ':', end='')
            monthRainfall = float(input(' '))

# Add to total rainfall amount
            totalRainfall += monthRainfall
# Calculate the average rainfall
            averageRainfall = totalRainfall / totalMonths
# Printing the result
print('Number of months: ', totalMonths)
print('Total rainfall: ', format(totalRainfall, '.2f'), 'inches')
print('Average rainfall: ', format(averageRainfall, '.2f'), 'inches')