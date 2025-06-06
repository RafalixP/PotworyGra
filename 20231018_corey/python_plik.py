greeting = "Hello"
name = 'Rafal'

message = greeting + name
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir())
print(help(str.lower))