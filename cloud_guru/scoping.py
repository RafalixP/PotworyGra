# if 1 < 2:
#     x = 5

# while x < 6:
#     #print(x)
#     x += 1

# print(x)


###############

# y = 5

# def set_x(y):
#     print('Inner y: ', y)
#     #x = y
#     #y = x

# set_x(10)

# print('Outer y: ', y)


##################


# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# age = ages.get('Kevin', 'Not found')
# print(age)


##

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# age = ages['Kevin']
# print(ages * 2)



#What is the output of this code?

# for num in range(1, 10, 2):
#     if num % 3:
#         print(num)


####

# Fill in the blank ___ with the function name to produce the expected output given the input.

# Input: 15000.0 Expected output: 150.0

# num = input("Enter a float value: ")
# new_num = float(num) // 100 * 1.0
# print(new_num)


###

# num = 12
# num2 = num
# num = num + 1
# num2 = num2 / 2

# print(num2)


####

names = ['Alice', 'Bob', 'Lance', 'Mike']
all_names = names
names.remove('Bob')
all_names_2 = all_names + ['Kevin']

print(all_names_2)