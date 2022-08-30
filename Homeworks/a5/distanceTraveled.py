# Yelena Baranchuk
# The distance a vehicle travels can be calculated as follows:
# distance = speed * time
# For example, if a train travels 40 miles per hour for three hours,
# the distance traveled is 120 miles.
# Write a program that asks the user for the speed of a vehicle
# (in miles per hour) and the number of hours it has traveled.
# It should then use a loop to display the distance the vehicle
# has traveled for each hour of that time period.


speedVehicle = int(input("What is the speed of the vehicle in mph? "))
hoursTraveled = int(input("How many hours has it traveled? "))

if hoursTraveled <= 0 or speedVehicle <= 0:
    print("Invalid hours and mph must be greater than 0")
else:
    for time in range(hoursTraveled):
        distance = speedVehicle * (time + 1)

        print("Hour            Distance Travel")
        print(time + 1, "           ", distance)
