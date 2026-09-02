#Day 5 - Lists []

#List - Ordered and changeable | Allows duplicates
#Tuple - Ordered and unchangeable | Allows duplicates
#Dictionary - Unordered and changeable and indexed | Doesn't allow duplicates
#Set - Unordered and unchangeable and un-indexed | Doesn't allow duplicates


#Level 1
list = ['item1', 'item2', 'item3', 'item4', 'item5']
print(list)
print(len(list))

first_item = list[0]
middle_item = list[int(len(list)/2)]
last_item = list[-1] 

mixed_data_types = ['Tudor Dragotescu', 20, 183, False, 'Address 1']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Stripe')
print(it_companies)
it_companies.insert(int(len(it_companies)/2), 'Crowdstrike')
print(it_companies)
it_companies[2].upper()
print(it_companies)
it_companies.extend('#; ')
print(it_companies)
print('IBM' in it_companies)
print(it_companies.sort())
print(it_companies.sort(reverse=True))
first_three = it_companies[0:3]
print(first_three)
last_three = it_companies[-3:]
print(last_three)
middle_company = it_companies[int(len(it_companies)/2)]
print(middle_company)
it_companies.pop(0)
it_companies.pop(-1)
print(it_companies)
it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

full_stack = front_end
print(full_stack)
index = full_stack.index('Redux')
full_stack.insert(index+1, 'Python')
full_stack.insert(index+2, 'SQL')
print(full_stack)

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)

average_age = 0
for i in range(len(ages)):
    average_age += ages[i]

average_age = average_age / len(ages)
print(average_age)