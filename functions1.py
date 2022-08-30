
import math


# this the main code which is the entry point to the program
def main():
    # main logic
    # x = input("Enter an integer")
    # print("Done")  # outside the function body
    # # print(message) You can't use the variable 'message' here because
    # # it is local the the show_message function
    #
    # show_message("Welcome to the class!")  # the call needs an argument that
    # # goes into the parameter of the function, called message
    #
    # show_message("This is a Python class")
    # call the add_numbers() and pass to it 2 arguments
    x = 100
    y = 200
    global variable1
    variable1 = 600 # this a local variable
    add_numbers(x, y, "text me")
    print("From main: ", variable1)
    pr = multiply_values(20, 40)
    print(pr)

    print("The product is", multiply_values(12, 45))

    area = calc_circle_area(300)
    print(f"Area is {area:.2f}")
    return

"""
write a function that takes the radius of a circle and returns
the area of a circle  (area = pi * r^2)
"""


def calc_circle_area(radius):
    # area = PI * radius ** 2
    # return area
    return math.pi * math.pow(radius, 2)


variable1 = 200 # global
#write a function that takes 2 arguments/parameters and prints their sum
# call it in the main
def add_numbers(number1, number2, text): # 2 parameters
    print("From add_numbers:", variable1)
    result = number1 + number2  # result is a local variable
    print(f"{text} {result}")
    return

# this function prints the hello message to the console
def show_message(message):  # message is called parameter
    # function block (body)
    # print the message
    #message = "Hello, World!"
    print(message)
    return

# Write that multiplies 2 values and returns the result
def multiply_values(num1, num2):
    result = num1 * num2

    return result


main()
