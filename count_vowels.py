s = 'azcbobobegghakl'
vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
num_vowels = 0
for c in s:
    num_vowels+=vowels.get(c, 0)

print("Number of vowels:", num_vowels)
