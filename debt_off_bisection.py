import sys

balance=320000
annualInterestRate=0.2

monthlyInterestRate = annualInterestRate / 12.0
minimumFixedMonthlyPayment = 0
numGuesses = 0

low = balance / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

# Remaining balance after 12 months
def getRemainingBalance( balance, minimumFixedMonthlyPayment, monthlyInterestRate ):
    previousBalance = balance
    for m in range(0, 12):
        monthlyUnpaidBalance = previousBalance - minimumFixedMonthlyPayment
        previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    return previousBalance 

remainingBalance = balance
minimumFixedMonthlyPayment = (low + high) / 2

while abs((low - high)/minimumFixedMonthlyPayment) * 100000 > 0.02:
    remainingBalance = getRemainingBalance(balance, minimumFixedMonthlyPayment, monthlyInterestRate)
    if remainingBalance > 0:
        low = minimumFixedMonthlyPayment
    else:
        high = minimumFixedMonthlyPayment
    minimumFixedMonthlyPayment = (low + high) / 2
    numGuesses+=1

print("Lowest Payment: " + str(round(minimumFixedMonthlyPayment, 2)))

