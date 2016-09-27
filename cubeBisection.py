cube = 27
epsilon = 0.0000000000000000000000000000000000000000000000000000000001
num_guesses = 0
low = 0.0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
        print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1

print('num_guesses = ' + str(num_guesses))
print(str(guess) + ' is close to square root of ' + str(cube))
