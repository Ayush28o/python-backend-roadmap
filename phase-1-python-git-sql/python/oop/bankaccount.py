class BankAccount:
    def __init__(self, owner, balance=0, history=None):
        self.owner = owner
        self.__balance  = balance
        self.history = history if history is not None else []

    def deposit(self, amount):
        self.__balance  += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if self.__balance  < amount:
            print("insufficient amount")
            return False
        self.__balance  -= amount
        self.history.append(("withdraw", amount))
        return True

    def get_balance(self):
        return self.__balance 

acc1 = BankAccount("Nikhil", 5000)
acc1.deposit(200)
acc1.withdraw(500)
print(acc1.get_balance())

acc2 = BankAccount("Nikita", 1000)
acc2.deposit(2000)
acc2.withdraw(500)
print(acc2.get_balance())

acc3 = BankAccount("Ankit", 5000)
acc3.deposit(2000)
acc3.withdraw(5000)
print(acc3.get_balance())
