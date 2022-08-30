# Yelena Baranchuk


# Get the base and height of two triangles from the user

baseOfFirstTriangle = int(input('Input the base of the first triangle: '))
baseOfSecondTriangle = int(input('Input the base of the second triangle: '))

heightOfFirstTriangle = int(input('Input the height of the first triangle: '))
heightOfSecondTriangle = int(input('Input the height of the second triangle: '))

# Formula of the area of the first triangle

areaOfFirstTriangle = (baseOfFirstTriangle * heightOfFirstTriangle) / 2

# Formula of the area of the second triangle

areaOfSecondTriangle = (baseOfSecondTriangle * heightOfSecondTriangle) / 2

# Check which triangle has the greater area

if areaOfFirstTriangle > areaOfSecondTriangle:
    print('The first triangle has the greater area than the second triangle')
elif areaOfFirstTriangle < areaOfSecondTriangle:
    print('The second triangle has the greater area than the first triangle')
else:
    print('Triangles are equal')

