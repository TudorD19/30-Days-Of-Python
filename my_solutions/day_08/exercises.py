#Day 8 - Dictionaries {}

dog = dict()
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Teckel'
dog['legs'] = 4
dog['age'] = 2
print(dog)

student = {
    'first_name':'Tudor',
    'last_name':'Dragotescu',
    'gender':'Male',
    'age':20,
    'married':False,
    'skills':["C","Python","Linux"],
    'country':'Romania',
    'address':'Bucharest'
}

print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('NodeJS')
print(student['skills'])
keys1 = student.keys()
values1 = student.values()
print(keys1)
print(values1)
items_list = student.items()
print(items_list)
student.pop('married')
print(student)

del student
