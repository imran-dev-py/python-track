class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_money):
        self.balance += dep_money
        # return self.balance
        print('Deposit Accepted')
        print(f'Current balance: ${self.balance}')

    def withdraw(self, withdraw_money):
        if self.balance <= withdraw_money:
            print('Funds unavailable')
        else:
            self.balance -= withdraw_money
            print('Withdrawl Accepted')
            print(f'You withdrawn: ${withdraw_money}')

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: ${self.balance}'


account1 = Account('Jose', 100)
print(account1)
print(account1.owner)
print(account1.balance)
account1.deposit(450)
account1.withdraw(140)
print(account1)
