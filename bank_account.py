class BankAccount: 
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self) 

    def deposit(self, amount):
        self.balance += amount 
        return self 

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount 
        else: 
            print("Insufficient Funds: Charging a $5 fee")

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 
    
    @classmethod
    def print_all_accounts(cls)
        for account in cls.accounts:
            account.display_account_info()
            
checkings = BankAccount(.01, 5000)
savings = BankAccount(.05, 1000)

checkings.deposit(10).deposit(30).deposit(40).yeild_interest().display_account_info()
savings.deposit(10).deposit(30).withdraw(40).withdraw(32).withdraw(50).withdraw(20).yeild_interest().display_account_info()

BankAccount.print_all_accounts()