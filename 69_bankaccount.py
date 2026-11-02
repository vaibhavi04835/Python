class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)

b1 = BankAccount("Amit", 5000)

b1.deposit(2000)
b1.display()