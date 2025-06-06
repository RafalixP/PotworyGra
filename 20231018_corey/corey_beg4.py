


#Mutable
'''list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)'''

#Inmutable
'''tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)'''

'''cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))'''




courses = ['History', 'Math', 'Physics', 'CompSci']
'''
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)'''

for item in courses:
    print(item)  
    
#for index, course in enumerate(courses, start=1):
    #print(index, course)
'''
print(' ')
for index, course in enumerate(courses, start=1):
    print(index, course)'''

'''print(courses.index('CompSci'))

print('Art' in courses)
print('Math' in courses)'''

'''nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)

print(courses)
print(sorted_courses)
print(min(nums))
print(sum(nums))'''


'''courses.reverse()
print(courses)
courses.sort(reverse=True)
print(courses)
nums.sort(reverse=True)
print(nums)

'''
'''courses_2 = ['Art', 'Education']

print(courses)
courses.pop()
print(courses)
'''

'''
courses.extend(0, courses_2)
print(courses)
'''
'''
courses.insert(0, courses_2)
print(courses)
'''





'''
print(len(courses))
print(courses[0])
print(courses[-1 ])
print(courses[0:2])
print(courses[2:])
'''
#courses.append('Art')
#print(courses)
#courses.insert(0,'Sztuka')
#print(courses)