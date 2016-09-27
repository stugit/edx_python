


def remaining_balance_after_a_year(previousBalance, annualInterestRate, minimumMonthlyPaymentRate):
    for i in range(1, 13):
        monthlyInterestRate = annualInterestRate / 12
        minmumMonthlyPayment = previousBalance * minimumMonthlyPaymentRate
        monthlyUnpaidBalance = previousBalance - minmumMonthlyPayment
        remainingBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        previousBalance = remainingBalance

        print("Month " + str(i) + " Remaining balance: " + str(round(remainingBalance, 2)))

remaining_balance_after_a_year(42, 0.2, 0.04)

remaining_balance_after_a_year(484, 0.2, 0.04)
