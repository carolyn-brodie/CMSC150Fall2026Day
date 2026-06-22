
class BankAccount:

    ##Constructor
    def __init__(self, name, account_number, balance = 0):
        self.owner = name
        self.account_number = account_number
        self.balance = balance

    ##Class related methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


    def get_balance(self):
        return self.balance



    ##Nice to have method to print things out
    def __str__(self):
        out = self.owner + " has account " + str(self.account_number)
        out = out + " that contains a balance of " + str(self.balance)
        return out


def tester():
    suzy_account = BankAccount("Suzy Que", 3456)
    print(suzy_account)


if __name__ == "__main__":
    tester()