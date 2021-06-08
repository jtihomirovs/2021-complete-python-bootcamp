class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account owner: {} \nAccount balance: {}'.format(self.owner, self.balance)

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print('Deposit Accepted')

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)

acct1.withdraw(75)

acct1.withdraw(500)
