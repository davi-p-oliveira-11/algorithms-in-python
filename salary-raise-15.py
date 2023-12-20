'''
 13) Create an algorithm that reads an employee's salary,
 calculates, and displays their new salary with a 15% increase."
'''

salary = float(input('Enter the value of your salary: ' ))

salary_raise = salary * 0.15
new_salary = salary + salary_raise

print(f'The value of the new salary is {new_salary}')
