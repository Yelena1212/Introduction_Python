
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



# 1 read the hours worked: read hours
# hours = input("Please enter the hours worked in integer: ")
# hours = int(hours)  # extract the integer value from the text typed
hours = int(input("Please enter the hours worked: ")) # "345"

# 2 read the hourly rate: input hourly_rate
hourly_rate = input("Please enter your hourly rate: ")
hourly_rate = float(hourly_rate)  # extract the integer value from the text typed
# 3 calculate the gross pay: gross_pay = hours * hourly_rate
gross_pay = hours * hourly_rate# assignment statement (variable = expression)
# PEMDAS
# 4 display the pay: print "Your pay is ", gross_pay
print("Your pay is $", format(gross_pay, '.2f'))




