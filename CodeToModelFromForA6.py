'''
helpful links
https://www.w3schools.com/python/python_dictionaries_add.asp
https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
https://www.tutorialspoint.com/How-to-find-the-average-of-non-zero-values-in-a-Python-dictionary
https://www.w3schools.com/python/python_lists_add.asp
'''

import operator

Car = {}

'''
values we want in dictionary:
Car = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
'''

i = 0
while (i<4):
    carVal = int(input("please enter car value: "))
    if i == 0:
        Car["Audi"]=carVal	
    elif i == 1:
	    Car["BMW"]=carVal
    elif i == 2:
	    Car["Jaguar"]=carVal
    else:
	    Car["Hyundai"]=carVal
    i=i+1

# Getting max and min values
keyMax = max(Car.items(), key = operator.itemgetter(1))[0]
keyMin = min(Car.items(), key = operator.itemgetter(1))[0]
print(keyMax)
print(keyMin)

#now get brands that correspond to those values
x = Car[keyMax]
print(x)
y = Car[keyMin]
print(y)

#determine the average of all values
filtered_vals = [v for _, v in Car.items() if v != 0]
average = sum(filtered_vals) / len(filtered_vals)
print(average)

carListLessThanAvg = []
for x in Car.values():
    if x < average:
        value = {i for i in Car if Car[i]==x}
        carListLessThanAvg.append(value)
print(carListLessThanAvg)