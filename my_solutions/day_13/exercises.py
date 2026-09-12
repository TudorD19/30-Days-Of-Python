#Day 13 - List comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print(filtered_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in list_of_lists for number in row]
print(flat_list)

list_of_tuples = [(i,1,i,i**2,i**3,i**4) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_countries = [[country_a.upper(), country_a[:3].upper(), country_b.upper()] for row in countries for country_a, country_b in row]
print(new_countries)

dict_countries = [{'country': country_a.upper(), 'city': country_b.upper()} for row in countries for country_a, country_b in row]
print(dict_countries)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [name_a + ' ' + name_b for row in names for name_a, name_b in row]
print(full_names)

m = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
print(m(2,3,5,6))