
# Author: Mohamed Zerrouki
# Assignment 1
# Description: This program reads the hours worked and the hourly rate from the user and
# calculates the gross pay, then displays it the user

"""
Author: Mohamed Zerrouki
Assignment 1
Description: This program reads the hours worked and the hourly rate from the user and
calculates the gross pay, then displays it the user
"""

# IPO: Input -> Process -> Output
#      Data  -> process -> Info
def calc_gross_pay(hours, hourly_rate):
    return hours * hourly_rate#

def main():
    # 1 read the hours worked: read hours
    # hours = input("Please enter the hours worked in integer: ")
    # hours = int(hours)  # extract the integer value from the text typed
    hours = int(input("Please enter the hours worked: ")) # "345"

    # 2 read the hourly rate: input hourly_rate
    hourly_rate = input("Please enter your hourly rate: ")
    hourly_rate = float(hourly_rate)  # extract the integer value from the text typed
    # 3 calculate the gross pay: gross_pay = hours * hourly_rate
    gross_pay = calc_gross_pay(hours, hourly_rate)
    
    # 4 display the pay: print "Your pay is ", gross_pay
    print("Your pay is $", format(gross_pay, '.2f'))

    return


 main()


"""
create the main function
create another function that takes the hours and pat rate as arguments and returns the gross pay
Main will call the function with the values input from the user and print the result to the console

"""



