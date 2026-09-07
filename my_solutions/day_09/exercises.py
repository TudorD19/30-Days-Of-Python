#Day 9 - Conditionals

#Level 1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need {} more years to learn to drive.'.format(18-age))

my_age = 20
your_age = age

if (your_age-my_age) == 1:
    print('You are one year older than me.') 
elif (your_age-my_age) > 1:
    print('You are {} years older than me.'.format(your_age-my_age))
elif your_age == my_age:
    print('We are the same age.')
elif (my_age - your_age) == 1:
    print('I am one year older than you.')
else:
    print('I am {} years older than you.'.format(my_age-your_age))

#Level 2

grade = int(input("Enter student's grade: "))
if grade >= 0 and grade <= 100:
    if grade <= 100 and grade >= 90:
        print("A")
    elif grade <= 89 and grade >= 80:
        print('B')
    elif grade <= 79 and grade >= 70:
        print('C')
    elif grade <= 69 and grade >= 60:
        print('D')
    else:
        print('F')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Add a fruit to the list: ")
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)

print(fruits)

#Level 3
person={
    'first_name': 'Tudor',
    'last_name': 'Dragotescu',
    'age': 20,
    'country': 'Romania',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

ok = 0
if person.get('skills') != None:
    print(person['skills'][2])
    print('Python' in person['skills'])

    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('Backend developer')
        ok = 1
    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('Fullstack developer')
        ok = 1
    if 'JavaScript' in person['skills'] and 'React' in person['skills'] and ok == 0:
        print('Frontend developer')


if person['country'] == 'Romania' and person['is_married'] == False:
    print('{} {} lives in {}. He is not married.'.format(person['first_name'], person['last_name'], person['country']))
