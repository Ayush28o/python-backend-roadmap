class bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw (self,amount):
        if self.balance<amount:
         print ( "insufficient amount")
        else:
           self.balance-= amount;


        
    def getbalance(self):
       return self.balance 


acc=bankaccount("Nikhil", 5000)
acc.deposit (200)
acc.withdraw (500)
print(acc.getbalance())

