month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#print(len(month_days))

def is_leap(year):
    """Checking is the input year is a leap year (true) or non-leap (false)"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''returns number of days in that month in that year'''

    if not 1 <= month <= 12:
        return 'Invalid month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(days_in_month(2020, 2))
    




# def hello_func(greeting):
#     return '{} function'.format(greeting)

# print(hello_func().upper())
