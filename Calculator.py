# TO-DO
# 1 Enter valid number
# 2 Invalid Operator
# 3 for power, % for modulo functionality
# 4 Square root functionality
# ***********************
def calculate():
    operation = input('''
Select Mathematical Operation:
+ for addition
- for subtraction
* for multiplication 
/ for division\n
''')
    number1 = int(input('\nPlease enter first number: '))
    number2 = int(input('Please enter second number: '))
    if operation == '+':
        print('\n{} + {} = '.format(number1, number2))
        print(number1 + number2)
    elif operation == '-':
        print('\n{} - {} = '.format(number1, number2))
        print(number1 - number2)
    elif operation == '*':
        print('\n{} * {} = '.format(number1, number2))
        print(number1 * number2)
    elif operation == '/':
        print('\n{} / {} = '.format(number1, number2))
        print(number1 / number2)
    else:
        print('Invalid Operator, Try Again')
def repeatcalculate():
    repeat_calc = input(
        '''
Perform Another Mathematical Operation:
Please type Y for Yes or N for NO. 
        '''
    )
    if repeat_calc.upper() == 'Y':
        calculate()
    elif repeat_calc.upper() == 'N':
        print('See You Later.')
    else:
        repeatcalculate()
calculate()
repeatcalculate()
