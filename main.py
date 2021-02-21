# OOP

class BankAccount:
    # initializing the class
    def __init__(self):
        self.balance = 0

    # function for the deposit amount
    def deposit(self, amount):
        # balance is zero initially
        # after the deposit the balance will equal amount you deposit
        self.balance = self.balance + amount

    # function for the withdraw amount
    def withdraw(self, amount):
        # takes amount to be withdrawn as an argument
        if self.balance >= amount:
            self.balance -= amount
            # self.balance = self.balance - amount
            # balance will decrease by the amount withdrawn
        else:
            print("Insufficient funds")

    def print_balance(self):
        return self.balance


account = BankAccount()  # creating an instance of the bank account

account.deposit(100)  # depositing funds

account.deposit(200)  # another deposit

account.deposit(400)  # more deposit

account.withdraw(800)  # withdrawal

print(account.print_balance())





