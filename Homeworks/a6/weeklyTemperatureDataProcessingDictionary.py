# Yelena Baranchuk
# 08/17/2022
# A6 - Dictionary
# In the Python program create a main function which does the following:
# Using the ideas in CodeToModelFromForA6.py
# Create a dictionary weeklyTemps and initialize it with data
# similar to how it's done in the file CodeToModelFromForA6.py.
# where the keys are the days of the week, and the values are the temperatures.
# Request the temperature values for each day of the week Monday through
# Sunday and add the values to the dictionary defined above.
# Print the smallest temperature value along with the corresponding day as shown
# Print the largest temperature value along with the corresponding day as shown
# Print the average temperature.
# Print a list of the days for which the temperature is above average.

# Import operator to calculate max and min in program
import operator

# Create a dictionary with days of week, where values are empty strings
weeklyTemps = {'Monday': '', 'Tuesday' : '', 'Wednesday' : '',
                'Thursday' : '', 'Friday' : '', 'Saturday' : '', 'Sunday' : ''}

# Create main function
def main():

    # Create for loop to fill our dictionary temperature's data
    for day in weeklyTemps.keys():
        print("Enter the temperature for ", day, ": ", sep="")
        weeklyTemps[day] = float(input())
    # Display updated dictionary
    print(weeklyTemps)

    # Found day with max temperature in our dictionary
    dayOfMaxTemp = max(weeklyTemps.items(), key= operator.itemgetter(1))[0]
    # Found day with min temperature in our dictionary
    dayOfMinTemp = min(weeklyTemps.items(), key=operator.itemgetter(1))[0]
    # Found max temperature using the day of the week
    temperatureMax = weeklyTemps[dayOfMaxTemp]
    # Found max temperature using the day of the week
    temperatureMin = weeklyTemps[dayOfMinTemp]
    # Display the coldest day of the week
    print(dayOfMinTemp, " was the coldest day with a temperature value of ", temperatureMin, sep="")
    # Display the warmest day of the week
    print(dayOfMaxTemp, " was the warmest day with a temperature value of ", temperatureMax, sep="")

    # Find the average temperature of the week
    avgOfTemp = float(format(sum(weeklyTemps.values()) / len(weeklyTemps.values()), '.2f'))
    # Display the average temperature of the week
    print("The average temperature of the week is: ", avgOfTemp)

    # Create empty list for adding above average temperature
    tempListAboveAvg = []

    # Create for loop to find above average temperature
    for temp in weeklyTemps.values():
        if temp > avgOfTemp:
            # Find the day above average temperature
            value = {i for i in weeklyTemps if weeklyTemps[i] == temp}
            # Add the day in created list
            tempListAboveAvg.append(value)
    # Display days with above average temperature
    print("The list with days are above average temperature: ", tempListAboveAvg)

# Call main function
main()