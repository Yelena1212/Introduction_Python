# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.
high_score = 95
 
# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

elif average < 96 and average >= 90:
    print('Good job!')
    print('You have a good score and you have "B"')
elif average < 90 and average >= 85:
    print('Nice job!')
    print('You got a "B-" score')
elif average < 85 and average >= 75:
    print('You can do better!')
    print('Your score is "C"')
elif average < 75 and average >=65:
    print:('Your score is "C-"')
else:
    print('I am sorry! You have to take a test again!')
