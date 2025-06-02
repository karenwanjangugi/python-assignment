class Account:
    def __init__(self,name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.frozen = False
        self.transactions = []
        self.loan = 0
        self.balance = 0
    
        
        
        
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
        else:
            return "Enter valid amount"
        
        self.transactions.append(f"{amount} deposited into your account")
        # print (f"{amount} has been deposited into your account")
        return f"{amount} has been deposited into your account"
    
        
            
        
            
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
            return "Enter valid amount"
        else:
            return "Insufficient funds"
    
    def transfer(self,amount,target_account):
        if amount <= 0:
            return "Invalid amount"
    
        if self.get_balance() < amount:
            return "Insufficient funds."

        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(f"{amount} transferred to {target_account.name}")
    
        return f" {amount} successfully transferred to {target_account.name}"
    
   
    
    def loan(self,amount):
        if amount<=0:
            return "Enter valid amount"
        self.loan += amount
        self.balance += amount
        self.transactions.append(f"Loan given:{amount}")
        return f"Your loan has been approved.Current balance is: {self.balance}"
    
    def pay_loan(self,amount):
        if amount <= 0:
            return "Enter valid amount"
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.loan:
            amount = self.loan
            self.balance -= amount
            self.loan -= amount
            self.transactions.append(f"{amount} deducted from account for loan repayment")
            return f"Loan repayment successful. Remaining amount is {self.loan}"
        
    def view_account(self):
        return f" name: {self.name} Balance:{self.balance} Loan:{self.loan}"
    
    def change_account(self, new_name):
        old_name = self.name
        self.name = new_name
        self.transactions.append(f"Account name changed from{old_name} to {new_name}")
        return f"Name has been updated to {new_name}"
    
    def statement(self):
        print (f"Account statement for {self.name}:")
        for transaction in self.transactions:
            print (transaction)
    
    
    def interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest: {interest}")
        return f"Your new balance is{self.balance}"
    
    def freeze_account(self):
        self.frozen = True
        return "Account frozen"
    
    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen"
    
    def  close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan = 0
        self.transactions.clear()
        return "Account Closed"
    
  
    
    