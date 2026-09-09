#Day 11 - Functions

#Level 1
def print_list(list_parameter):
    for elem in list_parameter:
        print(elem)

l = ['element1', 'element2', 'element3']
print_list(l)

def reverse_list(list_parameter):
    for i in range(int(len(list_parameter)) // 2) :
        temp = list_parameter[i]
        list_parameter[i] = list_parameter[int(len(list_parameter)) - 1 - i]
        list_parameter[int(len(list_parameter)) - 1 - i] = temp

    return list_parameter

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C", "D"]))

def remove_item(list_parameter, item):
    for i in range(0,int(len(list_parameter))):
        if item == list_parameter[i]:
            list_parameter.pop(i)
            break
    return list_parameter
    


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#Level 2
def greet(name = 'Guest'):
    print("Hello {}!".format(name))

greet()
greet("Alice")

def show_args(**args):
    for k, v in args.items():
        print("{}: {}".format(k,v))
    
show_args(name="Alice", age=30, city="New York")

#Level 3 

def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

print(is_prime(9))
print(is_prime(7))

def unique(list_parameter):
    set_parameter = set(list_parameter)
    if len(set_parameter) == len(list_parameter):
        return True
    else:
        return False

print(unique([1, 2, 3, 4]))
print(unique([1, 2, 3, 1]))

from data.countries_data import countries_data

def most_spoken_languages(countries_data_param):
    most_spoken = []
    language_count = {}

    for country in countries_data_param:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    for language in language_count:
        most_spoken.append((language_count[language], language))

    most_spoken.sort(reverse=True)

    return most_spoken[:10]

print(most_spoken_languages(countries_data))