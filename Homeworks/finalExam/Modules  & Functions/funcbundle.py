# Import mean function from statistics module to calculate average of the list
from statistics import mean

# Create get_average function
def get_average(listOfValue):
    # Calculate average of the value's list
    avgOfListVal = format(mean(listOfValue), '.2f')
    # Return the average
    return avgOfListVal

# Create the get_min function
def get_min(listOfValue):
    # Found min value from the value's list
    minVal = min(listOfValue)
    # Return min value from the list
    return minVal

# Create the get_below_avg_count function
def get_below_avg_count(listOfValue):
    # Create an empty list to add the value are below average number
    listBelowAvgVal = []
    # Create for loop to find the values are below average number
    for value in listOfValue:
        # Use the get_average function to find the values are below average number
        if value < float(get_average(listOfValue)):
            # Add a number are below average in the list
            listBelowAvgVal.append(value)
    # Return the list of values are below average number
    return listBelowAvgVal







