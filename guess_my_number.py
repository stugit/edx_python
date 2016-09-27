
def guess_number(l, h):
    guess = int(l + (h - l) / 2)
    return guess

low = 0
high = 100

print('Please think of a number between 0 and 100!')

h_or_l = ''
while h_or_l != 'c':
    guess = guess_number(low, high)
    print('Is your secret number ' + str(guess) + '?')
    print("Enter 'h' to indicate the guess is too high. ", end='')
    print("Enter 'l' to indicate the guess is too low. ", end='')
    print("Enter 'c' to indicate I guessed correctly. ", end='')
    h_or_l = input()
    if h_or_l == 'l':
        low = guess
    elif h_or_l == 'h': 
        high = guess
    elif h_or_l != 'c':
        print('Sorry, I did not understand your input.')

print("Game over. Your secret number was: ", guess)
