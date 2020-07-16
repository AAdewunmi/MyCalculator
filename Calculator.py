# TODO
# 1 Enter valid number
# ** for power, % for modulo functionality
# 3 Square root functionality
# ***********************

number1 = int(input('Please enter first number: '))
number2 = int(input('Please enter second number: '))

operation = input('''
Select Mathematical Operation:
+ for addition
- for subtraction
* for multiplication 
% for division\n
''')

if operation == '+':
    print('\n{} + {} = '.format(number1, number2))
    print(number1 + number2)
elif operation == '-':
    print('\n{} - {} = '.format(number1, number2))
    print(number1 - number2)
elif operation == '*':
    print('\n{} * {} = '.format(number1, number2))
    print(number1 * number2)
elif operation == '%':
    print('\n{} % {} = '.format(number1, number2))
    print(number1 % number2)
else:
    print('Invalid Operator, Try Again')