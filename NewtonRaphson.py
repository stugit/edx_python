#!/usr/bin/python3
epsilon = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
y = 33423432423543333333333333333333333.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
