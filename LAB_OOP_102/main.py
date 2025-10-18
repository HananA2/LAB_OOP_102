from bank_account import BankAccount

account = BankAccount("Hanan", 500)

print(f"Welcome {account.get_account_holder()}!")
print(f"Your starting balance is: {account.get_balance()} SAR")

try:
    amount = float(input("Enter amount to deposit: "))
    new_balance = account.deposit(amount)
    print(f"Deposit successful! New balance: {new_balance} SAR")
except ValueError as e:
    print(f"Error: {e}")

try:
    amount = float(input("Enter amount to withdraw: "))
    new_balance = account.withdraw(amount)
    print(f"Withdrawal successful! New balance: {new_balance} SAR")
except Exception as e:
    print(f"Error: {e}")

print(f"Final balance: {account.get_balance()} SAR")
