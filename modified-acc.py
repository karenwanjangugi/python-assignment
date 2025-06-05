import datetime

class Transaction:
    def __init__(self,amount, transaction_type, narration="No narration provided"):
        self.amount = amount
        self.transaction_type = transaction_type
        self.narration = narration
        self.time_stamp = datetime.now()
        
    def __str__(self):
        return f"{self.time_stamp.strftime('%y-%m-%d %H:%M:%S')} , {self.transaction_type}, {self.narration}, KSH.{self.amount}"
    
class Account:
    def __init__(self,name):
        self.__frozen = False
        self.__transactions = []
        self.__loan = 0
        self.__balance = 0
    def __str__(self):
        return
        
        
        
    def deposit(self, amount):
        if amount > 0:
            return "Enter valid amount"
        
        self.__balance += amount
        self.__transactions.append(Transaction(amount, "deposit")) 
        return f"{amount} has been deposited"
                    
                    
    def get_balance(self):
    
        return self.__balance
    
    
    def withdraw(self, amount):
        if amount <= 0: 
            return "Enter valid amount"
            
        if self.get_balance() >= amount:
            return "Insufficient funds"
        
        self.__balance -= amount
        self.__transactions.append(Transaction(amount,"withdraw"))
          
    
    def transfer(self,amount,target_account):
        if amount <= 0:
            return "Invalid amount"
    
        if self.get_balance() < amount:
            return "Insufficient funds."

        self.__withdraw(amount)
        target_account.deposit(amount)
        self.__transactions.append(Transaction(amount, "Transfer"))
    
        return f" {amount} successfully transferred to {target_account.name}"
    
   
    
    def loan(self,amount):
        if amount<=0:
            return "Enter valid amount"
        self.__loan += amount
        self.__balance += amount
        self.__transactions.append(Transaction(amount, "loan"))
        return f"Your loan has been approved.Current balance is: {self.__balance}"
    
    def pay_loan(self,amount):
        if amount <= 0:
            return "Enter valid amount"
        if amount > self.__balance:
            return "Insufficient funds"
        if amount > self.loan:
            amount = self.loan
            self.__balance -= amount
            self.__loan -= amount
            self.__transactions.append(Transaction(amount,"Loan repayment"))
            return f"Loan repayment successful. Remaining amount is {self.loan}"
        
    def view_account(self):
        return f" name: {self.name} Balance:{self.balance} Loan:{self.loan}"
    
    def change_account(self, new_name):
        old_name = self.name
        self.name = new_name
        self.__transactions.append(Transaction(0,"name changed from {old_name} to {new_name}"))
        return f"Name has been updated to {new_name}"
    
    def statement(self):
        print (f"Account statement for {self.name}:")
        for transaction in self.transactions:
            print (transaction)
    
    
    def interest(self):
        interest = self.__balance * 0.05
        self.__balance += interest
        self.__transactions.append(f"Interest: {interest}")
        return f"Your new balance is{self.balance}"
    
    def freeze_account(self):
        self.__frozen = True
        return "Account frozen"
    
    def unfreeze_account(self):
        self.__frozen = False
        return "Account has been unfrozen"
    
    def  close_account(self):
        self.__transactions.append(Transaction(0, "closed"))
        self.__balance = 0
        self.__loan = 0
        self.__transactions.clear()
        return "Account Closed"
    
    
    