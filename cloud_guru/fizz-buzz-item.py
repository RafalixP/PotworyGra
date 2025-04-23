#while True:
count = 1
while count < 4:
    count += 1
    value = int(input('Enter the integer value: '))


    if value % 5 == 0 and value % 3 == 0:
        print('Fizz-buzz')
    elif value % 3 == 0:
        print('Fizz')
    elif value % 5 == 0:
        print('Buzz')
    else:
        print(value)

print('To koniec')