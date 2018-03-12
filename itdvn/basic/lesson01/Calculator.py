x = float(input('1st number:'))
y = float(input('2nd number:'))
operation = input('Operation:')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x + y
elif operation == '/':
    result = x + y
else:
    print('Unsupported operation')

if result is not None:
    print('Result', result)