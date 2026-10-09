#Day 14 - Higher Order Functions
from functools import reduce
from data.countries_data import countries_data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f_upper(param):
    return param.upper()

uppercase_countries = map(f_upper, countries)
print(list(uppercase_countries))

uppercase_names = map(f_upper, names)
print(list(uppercase_names))

def filter_function1(country):
        if 'land' in country:
              return True
        else:
              return False

filtered_countries = filter(filter_function1, countries)
print(list(filtered_countries))

chained_countries = map(f_upper,filter(filter_function1, countries))
print(list(chained_countries))

def sum_num(x, y):
      return int(x) + int(y)

total = reduce(sum_num, numbers)
print(total)


countries_by_name = sorted(countries_data, key = lambda country: country["name"])
countries_by_capital = sorted(countries_data, key = lambda country: country["capital"])
countries_by_population = sorted(countries_data, key = lambda country: country["population"], reverse = True)

spoken_by_location = {}
for country in countries_data:
      for language in country["languages"]:
            if language in spoken_by_location: 
                  spoken_by_location[language] += 1
            else:
                  spoken_by_location[language] = 1
            

top_10_populated = countries_by_population[:10]

print(spoken_by_location)
print(top_10_populated)



      