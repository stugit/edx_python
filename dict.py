d = {'A':1, 'B':2, 'C':3}

print(d.keys())
print(d.values())

d['A'] = 3
print(d)
print(d['A'])

print(len(d))

print('B' in d)
print(3 in d.values())


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
animals['a'] = 'anteater'

del(animals['b'])
print(animals.values())
