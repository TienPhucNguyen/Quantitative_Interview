import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'Name': ['John', 'Mike', 'Sally', 'Jane', 'Joe', 'Dan', 'Phil'],
    'Salary': [300, 200, 550, 500, 600, 600, 550],
    'manager_id': [3, 3, 4, 7, 7, 3, 'Null']
})

sum_salaries = 0
number_of_people = 0

for i in range(len(data)):
    if data['id'][i] not in list(data['manager_id']):
        sum_salaries += data['Salary'][i]
        number_of_people += 1

average_salary = sum_salaries / number_of_people
print('The average salary of employees who do not manage anyone is: ', average_salary)