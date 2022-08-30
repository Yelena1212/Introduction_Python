import matplotlib.pyplot as plt

weeklyDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
            'Friday', 'Saturday',  'Sunday']

def main():
    weeklyTemp = getTemps()
    print(weeklyDay[weeklyTemp.index(max(weeklyTemp))], \
          'was the warmest day with a temperature of', max(weeklyTemp))
    print(weeklyDay[weeklyTemp.index(min(weeklyTemp))], \
          'was the coldest day with a temperature of', min(weeklyTemp))
    makeGraph(weeklyTemp)
def getTemps():
    weekTemp = []
    for day in range(7):
        userTemp = input('Enter the temperature for ' + str(weeklyDay[day]) + ': ')
        weekTemp.append(userTemp)
        day += 1
    return weekTemp
def makeGraph(tempVal):
    x_coords = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
            'Friday', 'Saturday',  'Sunday']
    y_coords = tempVal
    plt.plot(x_coords, y_coords)
    plt.title('Weekly Temperature Data')
    plt.xlabel('Days of the Week')
    plt.ylabel('Temperature Values')
    plt.show()
main()
