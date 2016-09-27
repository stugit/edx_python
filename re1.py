import re

s = 'azcbobobegghakl'
n = re.search('bob', s).span()

print("Number of times bob occurs is:", len(n))
