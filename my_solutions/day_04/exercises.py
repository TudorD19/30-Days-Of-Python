#Day 4 - Strings

string1 = ['Thirty', 'Days', 'Of', 'Python']
string2 = ' '.join(string1)
print(string2)

string3 = 'Coding'
string4 = 'For'
string5 = 'All'

string6 = string3 + ' ' + string4 + ' ' + string5
print(string6)

company = "Coding For All"
print(company)
print(len(company))
company = company.upper()
print(company)
company = company.lower()
print(company)
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)

company = "Coding For All"
first_word = company[0:6]
print(first_word)

print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)

print(company.replace('Coding', 'Python'))
print("Python for Everyone".replace('Everyone', 'All'))
print('Coding For All'.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

company = "Coding For All"
print(company[0])
print(len(company)-1)
print(company[10])

print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))


print('Coding For All'.startswith('Coding'))

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print('The area of the circle with radius %d is %d meters square'%(radius, area))
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))
print(f'The area of a circle with radius {radius} is {area} meters square.')

a = 8
b = 6

print(f'{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}\n{a} / {b} = {(a/b)}\n{a} % {b} = {a%b}\n{a} // {b} = {a//b}\n{a} ** {b} = {a**b}')
