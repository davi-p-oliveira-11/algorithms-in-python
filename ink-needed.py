'''
10) Create an algorithm that reads the width and height of a wall,
 calculates and displays the area to be painted,
 and the amount of paint needed for the job,
 considering that each liter of paint covers an area of 2 square meters.
'''

height = float(input('Enter the height of the wall in meters: '))
width = float(input('Enter the width of the wall in meters: '))

area = width * height
amountNeeded = area * 0.5

print(f'The area of the wall to be painted is {area} square meters.')
print(f'and the amount of paint needed to paint the wall is {amountNeeded} liters.')
