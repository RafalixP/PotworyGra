#!/usr/bin/env python3.10

message = input("Enter a message: ")

print('Lowercase:', message.lower())
print(message.upper())
print(message.capitalize())
print(message.title())

words = message.split()
print(words)
print('Ostatni wyraz to: ', words[-1])

sorted_words = sorted(words)
print('Wyrazy posortowane: ',sorted_words)