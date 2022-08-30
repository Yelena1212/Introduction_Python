# Yelena Baranchuk
# 08/10/2022
# A5 - List
# In the Python program create a main function which does the following:
# Request the temperature values for each day of the week Monday through Sunday and add the data to an empty list.
# You must use a for loop.
# Print the smallest temperature value along with the corresponding day as shown:
# Print the largest temperature value along with the corresponding day as show:
# Print the average temperature.
# Add Python code, using the matplotlib package, to plot the data in a line graph showing all of the following:
# A title: Weekly Temperature Data
# Labels for both the y-axis and the x-axis, respectively: Temperature Values, and Days of the Week
# Ticks for the x-axis showing the names of the days: Monday, Tuesday, etc

# This program displays a simple line graph.
import matplotlib.pyplot as plt

# Size of the temperature list
NUM_OF_DAYS = 7

# Create a main function
def main():

    # Create the list with days of week
    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Create empty list for temperature values
    temperatureList = [0] * NUM_OF_DAYS

    # Get value for each day of week
    for day in range(NUM_OF_DAYS):
        # Print message for user input
        print("Enter the temperature for ",weekDays[day],": ", sep='')
        # Add the input value to the temperatureList
        temperatureList[day] = float(input())
    # Display the temperatureList list
    print(temperatureList)

    # Get min value from the temperatureList
    minValue = min(temperatureList)
    # Found index of the min temperature
    indexOfMinValue = temperatureList.index(minValue)
    # Display the coldest day of the week
    print(weekDays[indexOfMinValue], "was the coldest day with a temperature value of", minValue)

    # Get max value from the temperatureList
    maxValue = max(temperatureList)
    # Found index of the max temperature
    indexOfMaxValue = temperatureList.index(maxValue)
    # Display the warmer day of the week
    print(weekDays[indexOfMaxValue], "was the warmest day with a temperature value of", maxValue)

    # Create a variable to use as an accumulator
    total = 0.0

    # Calculate the total of the list temperature
    for value in temperatureList:
        total += value

    # Calculate the average of the temperature
    average = format(total / NUM_OF_DAYS, '.2f')

    # Display the total of the temperature list
    print("The average temperature is: ", average, sep='')

    # Add a title
    plt.title('Weekly Temperature Data')

    # Add list with days to X coordinates of each point
    # and list with temperatures to Y coordinates of each point
    x_coords = weekDays
    y_coords = temperatureList

    # Build the line graph
    plt.plot(x_coords, y_coords)

    # Add labels to the axes
    plt.xlabel('Temperature Values')
    plt.ylabel('Days of the Week')

    # Add ticks to the x-coord
    plt.xticks([0, 1, 2, 3, 4, 5, 6],
               ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    # Add a grid
    plt.grid(True)

    # Display the line graph
    plt.show()

# Call the main function
main()


