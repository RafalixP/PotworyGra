class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    #def info(self):
    #    print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}")

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}"

    def __repr__(self):
        return f"Employee({self.name}, {self.age}, {self.position} with the salary of {self.salary})"


employee1 = Employee('Ji-soo', 38, 'developer', 1200)

print(employee1.name)  # Output: Ji-soo

employee1.name = "Cynthia"

print('Employee 1 has a new name of: ', employee1.name)  # Output: Cynthia
#print(employee1.__class__)  # Output: <class '__main__.Employee'>

#print(employee1.info())  
#print(Employee.__dict__)
print(employee1)
print(str(employee1))
print(repr(employee1))

