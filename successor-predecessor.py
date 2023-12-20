'''
6) Create a program that reads an integer and displays its predecessor and successor.
Example:
Enter a number: 9
The predecessor of 9 is 8
The successor of 9 is 10
'''
number = int(input('Enter a number: ' ))

predecessor = number - 1
successor = number + 1

print(f'The predecessor of {number} is {predecessor}')
print(f'The successor of {number} is {successor}')
