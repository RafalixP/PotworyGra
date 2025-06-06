#1
# age = 23
# name = "Raf"

# print("hello world", end = "       ")
# print("I am", name)

#2
# help(print)

#3 range

# rng = range(12,10,-3)

# print(list(rng))


#4 map function

# strings= ["my", "world", "apple", "pear"]

# #attempt 1

# # lengths = []

# # for string in strings:
# #     lengths.append(len(string))

# # print(string)
# # print(lengths)

# #attempt 2

# lengths = map(len, strings)

# print(list(lengths))



#5 filter function

# def longer_than_4(string):
#     return len(string) >= 4

# strings = ["my", "world", "apple", "pear"]
# filtered = filter(longer_than_4, strings)

# print(list(filtered))
 

# 6 f-function

val = "Geeks"
print(val + " " + "for" + " " + val + " " + "is a portal for" + " " + val )

print(f"{val} for {val} is a portal for {val}")

import datetime

today = datetime.datetime.today