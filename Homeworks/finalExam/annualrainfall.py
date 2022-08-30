# Yelena Baranchuk
# Design a main program that lets the user enter the total
# rainfall (in inches)  for each of 12 months into a dictionary
# that stores months and rainfalls as key-value pairs.
# The dictionary should be created empty and then filled
# with data from the user. The program should ask the user
# to enter the month's name followed by the rainfall amount in 2
# separate inputs for each of the 12 months of the year.
# You should not use any other data structure to help with this task.
# The program should then calculate and display (you can't combine this
# task with the previous task:)
# the total rainfall for the year,
# the average monthly rainfall,
# and the months with the highest and lowest amounts.
# You should not use functions other than the main function in this question

# Import operator to calculate max and min in program
import operator

# Create empty dictionary to fill in months and rainfall values
rainfallMonths = {}

# Create main function
def main():

    # Create for loop to fill out dictionary items
    for i in range(12):
        # Get the month's name from the user
        month = input("Enter the month's name: ")
        # Get the rainfall value for the inputted month
        print(f"Enter the rainfall amount for {month}: ")
        rainfall = float(input())

        # Check if month not in dictionary already
        if month not in rainfallMonths:
            # Add month and rainfall value in dictionary
            rainfallMonths[month] = rainfall
    # Display dictionary
    print(rainfallMonths)

    # Calculate the total rainfall for year
    total = float(format(sum(rainfallMonths.values()), '.2f'))
    # Display the total of the year
    print("The total rainfall for the year is: ", total)

    # Calculate the average monthly rainfall
    avgOfRainfall = float(format(total / len(rainfallMonths.values()), '.2f'))
    # Display the average monthly rainfall
    print("The average monthly rainfall is:", avgOfRainfall)

    # Found month with max value in our dictionary
    monthOfMaxAmount = max(rainfallMonths.items(), key=operator.itemgetter(1))[0]
    # Found month with min value in our dictionary
    monthOfMinAmount = min(rainfallMonths.items(), key=operator.itemgetter(1))[0]
    # Found max value using the month of the year
    maxRainfall = rainfallMonths[monthOfMaxAmount]
    # Found min value using the month of the year
    minRainfall = rainfallMonths[monthOfMinAmount]
    # Display the month with the highest rainfall in the year
    print(monthOfMaxAmount, " was the month with highest rainfall of ", maxRainfall, sep="")
    # Display the month with the lowest rainfall in the year
    print(monthOfMinAmount, " was the month with lowest rainfall of ", minRainfall, sep="")

# Call main function
main()