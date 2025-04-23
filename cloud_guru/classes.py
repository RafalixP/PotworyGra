employee1 = {
    'name': 'Ji-soo',
    'age': 38,
    'position': 'developer',
    'salary': 1200
    }
employee2 = {
    'name': 'Lauren',
    'age': 30,
    'position': 'tester',
    'salary': 1000
    }

def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent/100)


def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a  {employee['position']} with the salary of {employee['salary']}")


employees = [employee1, employee2]

print(employees)

increase_salary(employee1,100)


for e in employees:
    #print(f"{e['name']}' salary is ${e['salary']}")
    employee_info(e)

print(employee_info.__class__)