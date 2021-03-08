import csv

users = [{'name': 'sol mansi', 'username': 'solm',
          'department': 'it infrastructure'},
         {'name': 'lio nelson', 'username': 'lion',
          'department': 'ux research'},
         {'name': 'charlie grey', 'username': 'greyc',
          'department': 'development'}]

keys = ['name', 'username', 'department']

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
