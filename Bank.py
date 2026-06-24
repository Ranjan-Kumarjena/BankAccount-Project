class Bankaccount:
    def __init__(self,account_number,owner_number,balance=0):
        self.account_number=account_number
        self.owner_number = owner_number
        self.balance = balance

    def depositte(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"{amount} deposited.  new balance is {self.balance} " )
        else:
            print("must be deposited ")
            
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficent balance ")
        else:
            self.balance-=amount
            print(f"{amount }withdraw. new alance id {self.balance}")
    def check_balance(self):
        print(f"Account: {self.account_number} | Owner: {self.owner_number} | Balance: ₹{self.balance}")
        
        
b1= Bankaccount("SBI001", 123038484, 5000)
b1.depositte(1000000)
b1.withdraw(1000000)
b1.check_balance()

        