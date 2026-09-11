from random import *
from string import *
def random_user_id(number_of_c):
    characters = ascii_letters + digits
    user_id =""
    for i in range(number_of_c):
            user_id += choice(characters)
    return user_id



def user_id_gen_by_user():
    number_of_characters = int(input("Number of characters: "))
    number_of_ids = int(input("Number 0f IDs: "))
    for i in range(number_of_ids):
        print(random_user_id(number_of_characters))
    
user_id_gen_by_user()

def rgb_color_gen():
    colors = ()
    for i in range(3):
          colors += (randint(0,255),)
    return colors
print("rgb",rgb_color_gen())

def list_of_hexa_colors(number_of_colors):
     hexadecimal_characters = digits + "abcdef"
     color_array = []
     for i in range(number_of_colors):
        color = '#'
        for k in range(6):
               color += choice(hexadecimal_characters)
        color_array.append(color)
     return color_array
print(list_of_hexa_colors(3))       

def list_of_rgb_colors(number_of_colors):
    color_array = []
    for i in range(number_of_colors):
        color = 'rgb'
        color += str(rgb_color_gen())
        color_array.append(color)
    return color_array

print(list_of_rgb_colors(3))

def generate_colors(type_of_colors, number_of_colors):
     if type_of_colors == 'hexa':
          return list_of_hexa_colors(number_of_colors)
     elif type_of_colors == 'rgb':
          return list_of_rgb_colors(number_of_colors)
     else:
          print('Invalid type of color')

print(generate_colors('rgb', 3))

def shuffle_list(list_param):
     shuffled_list = []
     l = len(list_param)
     for i in range(l):
          element = choice(list_param)
          shuffled_list.append(element)
          list_param.remove(element)
     return shuffled_list
print(shuffle_list([1,2,3,4,5]))

def randomizer():
     range_of_num = [1,2,3,4,5,6,7,8,9]
     array = []
     element = 0
     for i in range(7):
          element = choice(range_of_num)
          array.append(element)
          range_of_num.remove(element)
     return array
print(randomizer())
