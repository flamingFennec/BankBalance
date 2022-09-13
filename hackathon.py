from hashlib import new


name = input("Welcome! What is your name? ")
balance = 5000.25
print(f"Hello {name}, your starting balance is {balance}.")
pay_check = int(input("How much of your paycheck would you like to deposit? "))
expenditure_item = input("It seems like you have gone shopping. What have you bought? ")
expenditure = int(input(f"How much did {expenditure_item} cost? "))

def checking_balance(user_name, cashhh, deposits, expense_item, expense_amount):
    ending_balance = cashhh + deposits - expense_amount
    print(f"Good evening, {user_name}. After spending money on {expense_item} in the amount of {expense_item}, your current balance is: {ending_balance}.")

checking_balance(name, balance, pay_check, expenditure_item, expenditure)