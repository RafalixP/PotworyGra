#1
# values = []
# for x in range(5,10):
#     values.append(x)

# print(values)


# values = [x for x in range(10,20)]
# print(values)

# values = [x*x for x in range(10,20)]
# print(values)



#2 even 0-50, add them to the list

# evens = []

# for number in range (50):
#    is_even = number % 2 == 0
#    if is_even == 0:
#       evens.append(number)

# print(evens)


# evens = [number for number in range(50) if number % 2 == 0]
# print(evens)

#3 strings that start with A and end in Y

# options = ["any", "albany", "apple", "world", "hello", ""]
# valid_strings = []

# for string in options:
#     if len(string) <= 1:
#         continue

#     if string[0] != "a":
#         continue
#     if string[-1] != "y":
#         continue

#     valid_strings.append(string)

# print(valid_strings)


# options = ["any", "albany", "apple", "world", "hello", ""]
# valid_strings = [
#     string
#     for string in options
#     if len(string) >= 2
#     if string[0] == "a"
#     if string[-1] == "y"
# ]
# print(valid_strings)



#4
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# flattened = []

# # for row in matrix:
# #     for num in row:
# #         flattened.append(num)

# flattened = [num for row in matrix for num in row]

# print(flattened)


#5 categorize numbers even/odd

# categories = []

# for number in range(10):
#     if number % 2 == 0:
#         categories.append("Even")
#         categories.append(number)
#     else:
#         categories.append("Odd")
#         categories.append(number)

# print(categories)

# categories = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

# print(categories)


#6 square given number

# def square(x):
#     x = input('Podaj liczbę której kwadrat chciałbyś poznać: ')
#     print( x ** 2 )


# square()

def square(x):
    return x**2

squared_numbers = [sqare(x) for x in range(10) if valid(x)]




