# Day 18 - RegEx 
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  


paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
frequent_words = {}
words_list = re.split('[ .]', paragraph)
print(words_list)

for word in words_list:
    if word == '':
        continue
    else:
        if word in frequent_words:
            frequent_words[word] += 1
        else: 
            frequent_words[word] =1
print(frequent_words)
frequent_words_sorted = sorted(frequent_words.items(), key = lambda pair: pair[1], reverse = True)
print(frequent_words_sorted)
for word, frequency in frequent_words_sorted:
    print((frequency,word))

text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
r_pattern = r'-?\d+'
points = re.findall(r_pattern, text)
print(points)
sorted_points = (sorted(points, key = lambda x : int(x)))
sorted_points = list(map(int, sorted_points))
print(sorted_points)

distance = sorted_points[-1] - sorted_points[0]
print(distance)

def is_valid_variable(variable_name):
    r_pattern_2 = r'[A-Za-z][A-Za-z0-9_]*'
    if  re.fullmatch(r_pattern_2, variable_name) is not None:
        return True
    else:
        return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True