class Account:
    def __init__(self,name):
        self.name = name
        # self.balance = 0
        self.deposits = []
        self.withdrawals = []
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
        else:
            print("Enter valid amount")
            
        # return balance = self.get_balance()
        
            
    def get_balance(self):
        balance = 0
        for deposit in self.deposits:
            balance += deposit
        
        return balance
    
    
    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self.withdrawals.append(amount)
            self.deposits.append(-amount)
        elif amount <= 0:
            print("Enter valid amount")
        else:
            print("Insufficient funds")
    
    def transfer(amount):
        j = "ki"
        
            

class Account2:
    def __init__(self,name):
        self.name = name
        # self.balance = 0
        self.deposits = []
        self.withdrawals = []
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
        else:
            print("Enter valid amount")
            
        # return balance = self.get_balance()
        
            
    def get_balance(self):
        balance = 0
        for deposit in self.deposits:
            balance += deposit
        
        return balance
    
    
    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self.withdrawals.append(amount)
            self.deposits.append(-amount)
        elif amount <= 0:
            print("Enter valid amount")
        else:
            print("Insufficient funds")
            
        
        
        