
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(1, 13):
    monthlyInterestRate = annualInterestRate / 12
    minmumMonthlyPayment = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minmumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print("Remaining balance: " + str(round(balance, 2)))
