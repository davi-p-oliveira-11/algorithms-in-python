'''
11) Develop a logic that reads the values of A, B, and C
 from a quadratic equation and displays the value of Delta.
'''

value_a = int(input('Enter the value of A '))
value_b = int(input('Enter the value of B '))
value_c = int(input('Enter the value of C '))

#bhaskara:  delta = b² - 4ac
value_delta = (value_b ** 2) - 4 * (value_a * value_c)
print(f'O valor de delta equivale a {value_delta}')
