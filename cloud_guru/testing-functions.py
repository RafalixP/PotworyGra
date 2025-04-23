# 1) Write a 'split_name' function that takes a string and returns a dict with first_name and last_name


def split_name(name):
    name = str(input('Please enter the name: '))
    first_name, last_name = name.split()
    name_dict = {'first_name': first_name, 'last_name': last_name}
    
    print(first_name)
    print(last_name)
    return name_dict
 
assert split_name("Kevin Bacon") == {
    'first_name': 'Kevin',
    'last_name': 'Bacon',
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}" 