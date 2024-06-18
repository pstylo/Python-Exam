class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # for example in Dollars

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f'Deposit Accepted: ${dep_amt}')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'Withdrawal Accepted: ${wd_amt}')
        else:
            print('Funds Unavailable!')

def main():

    acc01 = Account('Erwin', 100)
    
    # 2. Print the object 'acc01' on the console
    print(acc01)
    
    # 3. Print the account owner attribute only
    print(acc01.owner)
    
    # 4. Print the account balance attribute only
    print(acc01.balance)
    
    # 5. Make a deposit of 50$
    acc01.deposit(50)
    
    # 6. Make a withdrawal of 75$
    acc01.withdraw(75)
    
    # 7. Make a withdrawal that exceeds the available balance
    acc01.withdraw(100)

if __name__ == "__main__":
    main()