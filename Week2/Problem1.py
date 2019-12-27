# Write a program to calculate the credit card balance after one year if a
# person only pays the minimum monthly payment required by the credit card
# company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining
# balance. At the end of 12 months, print out the remaining balance. Be sure
# to print out no more than two decimal digits of accuracy - so print
#
#   Remaining balance: 813.41
#
#   instead of
#
#   Remaining balance: 813.4141998135
#   So your program only prints out one thing: the remaining balance at the end
#   of the year in the format:
#
#   Remaining balance: 4784.0
# A summary of the required math is found below:
#
# Monthly interest rate= (Annual interest rate) / 12.0 Minimum monthly
# payment = (Minimum monthly payment rate) x (Previous balance) Monthly
# unpaid balance = (Previous balance) - (Minimum monthly payment) Updated
# balance each month = (Monthly unpaid balance) + (Monthly interest rate x
# Monthly unpaid balance)
#
# We provide sample test cases below. We suggest you develop your code on
# your own machine, and make sure your code passes the sample test cases,
# before you paste it into the box below.


# def debt(balance, annualInterestRate, monthlyPaymentRate, noMonths=12):
#     """
#     :param balance: the outstanding balance on the credit card
#     :param annualInterestRate: annual interest rate as a decimal
#     :param monthlyPaymentRate: minimum monthly payment rate as a decimal
#     :return: remaining balance after one year rounded on two decimal points
#     """
#     monthEndBalance = balance - balance * monthlyPaymentRate
#     if noMonths == 1:
#         print("Remaining balance:", round(monthEndBalance + annualInterestRate / 12 * monthEndBalance, 2))
#     else:
#         # print("Month", noMonths, "Remaining balance:", round(monthEndBalance + annualInterestRate / 12 * monthEndBalance, 2))
#         return debt(monthEndBalance + annualInterestRate / 12 * monthEndBalance,
#                     annualInterestRate, monthlyPaymentRate, noMonths - 1)
#
#
# debt(42, 0.2, 0.04)

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
    monthEndBalance = balance - balance * monthlyPaymentRate
    # print("Month", month + 1, "Remaining balance:", round(monthEndBalance + annualInterestRate / 12 * monthEndBalance, 2))
    balance = monthEndBalance + annualInterestRate / 12 * monthEndBalance
    if month == 11:
        print("Remaining balance:", round(monthEndBalance + annualInterestRate / 12 * monthEndBalance, 2))
