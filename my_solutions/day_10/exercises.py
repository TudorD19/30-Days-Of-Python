#Day 10 - Loops

#Level 1

symbol = '#'
for i in range(7):
    print(symbol)
    symbol += '#'

n = 0
for i in range(11):
    print('{} x {} = {}'.format(n,n,n*n))
    n += 1

#Level 2

sum = 0
for i in range(101):
    sum += i
print(sum)

#Level 3
from data.countries import countries

for country in countries:
    if 'land' in country.lower():
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
l = len(fruits)//2
for i in range(l):
    temp = fruits[i]
    fruits[i] = fruits[len(fruits) - 1 - i]
    fruits[len(fruits) - 1 - i] = temp

print(fruits)

from data.countries_data import countries_data

languages = set()
for country in countries_data:
   for language in country["languages"]:
       languages.add(language)

print(len(languages))

language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

most_spoken = []
for language in language_count:
    most_spoken.append((language_count[language], language))

most_spoken.sort(reverse=True)
print(most_spoken[:10])

populations = []

for country in countries_data:
    populations.append((country["population"], country["name"]))

populations.sort(reverse=True)

print(populations[:10])