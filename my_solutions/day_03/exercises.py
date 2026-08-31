age = 20
my_height = 1.83
complex_number = 1 + 1j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = (base * height) / 2
print('The are of the triangle is ', area)

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is ', perimeter)

r_length = int(input('Rectangle length: '))
r_width = int(input('Rectangle width: '))
r_area = r_length * r_width
print('Rectangle area = ', r_area)
r_perimeter = 2 * (r_length + r_width)
print('Rectangle perimeter = ', r_perimeter)

circle_radius = int(input('Circle radius: '))
circle_area = 3.14 * circle_radius * circle_radius
print('Circle area: ', circle_area)
circle_circumference = 2 * 3.14 * circle_radius
print('Circle circumference: ', circle_circumference)

x = int(input('Enter the value of x: '))
y = x**2 + 6*x + 9
print(y)

length1 = len('python')
length2 = len('dragon')
print(length1 > length2)
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print(not('on' in 'dragon' and 'on' in 'python'))
length1 = float(length1)
print(length1)
length1 = str(length1)
print(length1)

value = int(input('Enter a number: '))
print('Value is even: ', value % 2 == 0)
print((7//3) == int(2.7))
print(type('10') is type(10))
print(int(9.8) == 10)


hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
print('Your weekly earning is ', hours * rate_per_hour)

years = int(input('Enter number of years you have lived: '))
print('You have lived for ', 3600*24*365*years, ' seconds') 

print('''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125''')
i = 1
while(i<6):
    print (i, '1', i, i**2, i**3)
    i += 1