# Day 7 - Sets {}
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Meta', 'Stripe', 'Adobe'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
it_companies.discard('Google')
print(it_companies)

j_A_B = A.union(B)
print(j_A_B)
i_A_B = A.intersection(B)
print(i_A_B)
print(A.issubset(B))
print(A.isdisjoint(B))
A.union(B)
B.union(A)
print(A)
print(B)
print(A.symmetric_difference(B))
del A
del B

l1 = len(age)
age = set(age)
print(age)
l2 = len(age)
print('{} and {}'.format(l1, l2))

words = list()
words = ('I am a teacher and I love to inspire and teach people'.split())
print(words)
words_unique = set(words)
print(words_unique)

