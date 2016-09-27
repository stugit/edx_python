import sys

balance=23332
annualInterestRate=0.04

monthlyInterestRate = annualInterestRate / 12.0
minimumFixedMonthlyPayment = 0

# Remaining balance after 12 months
def getRemainingBalance( balance, minimumFixedMonthlyPayment, monthlyInterestRate ):
    previousBalance = balance
    for m in range(0, 12):
        monthlyUnpaidBalance = previousBalance - minimumFixedMonthlyPayment
        previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    return previousBalance 

remainingBalance = balance
while remainingBalance > 0:
    minimumFixedMonthlyPayment += 0.01
    remainingBalance = getRemainingBalance(balance, minimumFixedMonthlyPayment, monthlyInterestRate)

print("Lowest Payment: " + str(round(minimumFixedMonthlyPayment, -1)))

