animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    biggest_key = None
    biggest_value_len = 0
    for a in aDict.keys():
        if biggest_value_len < len(aDict[a]):
                biggest_value_len = len(aDict[a])
                biggest_key = a

    return biggest_key

print(biggest(animals))
        
