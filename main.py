from application.salary import calculate_salary

from application.db.people import get_employees

import datetime

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    print(datetime.date.today())
    calculate_salary()
    get_employees()

