#Day 6 - Tuples ()

empty_tuple = ()
tpl1 = ('Alex', 'Joe', 'Kevin')
tpl2 = ('Alexa', 'Maria', 'Ema')
siblings = tpl1 + tpl2
print(siblings)
print('I have {} siblings'.format(len(siblings)))

list1 = list(siblings)
list1.append('Ana')
list1.append('Marc')
family_members = tuple(list1)
print(family_members)

siblings = family_members[:6]
parents = family_members[-2:]


fruits = ('Banana', 'Apple', 'Strawberry')
vegetables = ('Carrot', 'Cucumber', 'Salad')
animal_products = ('Beef', 'Ham', 'Pepperoni')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_lt[4]
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)