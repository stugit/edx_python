animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(d):
    asum = 0
    for a in d.values():
        asum = asum + len(a)
    return asum


print(how_many(animals))

