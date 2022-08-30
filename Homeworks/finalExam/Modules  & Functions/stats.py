# Yelena Baranchuk
# Modules & Functions:
# Define the following functions in a module called funcbundle:
# get_average(data): takes a list of integer values and returns the average value.
# get_min(data): takes a list of integers and returns the smallest value.
# get_below_avg_count(data): takes a list of integers and returns the count of values below average.
# In the main file, write code in the main function to prompt the user for 10 integer values,
# store them in a list and then call the above functions with the list as an argument
# and print the results with proper messages describing the values.
# All output is done in the main function

# Import module funcbundle
import funcbundle

# Create an empty list to add integers
listOfVal = []

# Create main function
def main():
    # Create for loop to add values to the list
    for i in range(10):
        user_input = input("Please input an value: ")
        # Check if inputted value is integer
        try:
            number = int(user_input)
            listOfVal.append(number)
            # if inputted value is not an int except error message
        except ValueError:
            print("Please input an integer value!")

    # Display the list with 10 integer values
    print("The list with 10 integer values:", listOfVal)

    # Call get_average function from the module file
    averageOfNumbers = funcbundle.get_average(listOfVal)
    # Display the average number of the list
    print("The average number of the list is: ", averageOfNumbers)

    # Call get_min function from the module file funcbundle
    minValOfList = funcbundle.get_min(listOfVal)
    # Display the smallest value in the list
    print("The smallest value in the list is: ", minValOfList)

    # Call the get_bellow_avg_count function from the module file
    listBelowAvgVal = funcbundle.get_below_avg_count(listOfVal)
    # Display the list with values are below average number
    print("The list with values are below average numbers: ", listBelowAvgVal)
    # Get the length of the list with values are below average
    countOfBelowAvgVal = len(listBelowAvgVal)
    # Display the count of the bellow average numbers
    print("The count of the below average numbers is: ", countOfBelowAvgVal)

# Call main function
main()
