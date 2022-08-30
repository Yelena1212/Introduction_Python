# Yelena Baranchuk
# Lists
# Design a main program that creates a list of 10 competition scores as integer numbers, 0-10. You should not request user input here.
# The program then performs the following processing steps to produce a fair average score:
# Find the first lowest score in the list, display the score with its position in the list, and then remove it from the list.
# Find the first highest number in the list, display the score with its position in the list, and then remove it from the list.
# Calculate the average of the remaining scores and display it.

# Import randint function from the random module
from random import randint

# Create main function
def main():
    # Create an empty list
    listOfScores = []
    # Create a variable to calculate the sum of number in the list
    sumOfNumbers = 0

    # Create for loop to generate 10 random numbers
    for num in range(10):
        # Add generated numbers to the list
        listOfScores.append(randint(0, 10))
    # Display created list
    print(listOfScores)

    # Create a variable to find the smallest number in the list
    minVal = listOfScores[0]
    # Create a variable to find an index of the smallest number in the list
    count = 0
    # Create for loop to find min value in the list
    for num in listOfScores:
        if minVal > num:
            minVal = num
    # Create a for loop find the first lowest score in the list (first smallest number)
    for num in listOfScores:
        if num == minVal:
            # Display the first lowes score and position
            # I added count + 1 because I thought that in the requirements we have to show to user
            # real position of the score (1 - 10)
            # while an index of number started from 0 and showing not truth position
            # I hope I understood requirements correct, and you will not cut points for this.
            print(f"The first lowest score is {num} located at position {count + 1}")
            # Remove the first lowest score from the list
            listOfScores.pop(count)
            # Stop program
            break
        # Increase count
        count += 1

    # Create a variable to find the highest score in the list
    maxVal = listOfScores[0]
    # Create a variable to find the position of the highest score
    count = 0
    # Create for loop to find the highest score in the list
    for num in listOfScores:
        if maxVal < num:
            maxVal = num
    # Create for loop to find the first larger number in the list
    for num in listOfScores:
        if num == maxVal:
            # Display the first highest score in the loop and position
            print(f"The first highest score is {num} located at position {count + 1}")
            # Remover the highest
            listOfScores.pop(count)
            # Stop program
            break
            # Increase the count
        count += 1

    # Display updated list
    print("Updated list: ", listOfScores)

    # Create for loop to find sum of the remaining score
    for i in range(len(listOfScores)):
        sumOfNumbers += listOfScores[i]
    # Find average of the remaining score
    averageNumList = round(sumOfNumbers / len(listOfScores), 2)
    # Display the average
    print("The effective score is: ", averageNumList)

# Call main function
main()