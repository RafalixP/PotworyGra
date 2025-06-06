from employees import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('List of our employees:')
        for i in self.employees:
            print(f"{i.fname} {i.lname}")
            print('-------------')

    def pay_employees(self):
        print('Paying employees')
        for i in self.employees:
            print(f'Paycheck for: {i.fname} {i.lname}')
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('-------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Lee', 'Smith', 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Bob', 'Brown', 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()
    
if __name__ == '__main__':
    main()
