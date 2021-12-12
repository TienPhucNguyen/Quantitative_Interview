import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'Name': ['John', 'Mike', 'Sally', 'Jane', 'Joe', 'Dan', 'Phil'],
    'Salary': [300, 200, 550, 500, 600, 600, 550],
    'manager_id': [3, 3, 4, 7, 7, 3, 'Null']
})

result = []
for i in range(len(data)):
    for j in range(len(data)):
        if data['manager_id'][i] == data['id'][j] and data['Salary'][i] > data['Salary'][j]:
            result.append(data['Name'][i])

print('People whose salaries are greater than their immediate managers: ', result)
