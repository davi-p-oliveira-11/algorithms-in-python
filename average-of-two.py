'''
5) Create a program that reads a student's two grades in a subject and displays their average on the screen.
Example:
Grade 1: 4.5
Grade 2: 8.5
The average between 4.5 and 8.5 is equal to 6.5.
'''

grade_1 = float(input('Enter the first grade: '))
grade_2 = float(input('Enter the second grade: '))

average = (grade_1 + grade_2) / 2

print(f'The average between {grade_1} and {grade_2} is equal to {average}')
