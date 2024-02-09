class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount should be greater than zero.")


if __name__ == "__main__":
    
    my_account = Account("John")

   
    my_account.deposit(100)
    my_account.withdraw(50)
    my_account.withdraw(80)  
    my_account.deposit(200)
    my_account.withdraw(150)

    my_account.withdraw(-20)

  
    print(f"Final balance for {my_account.owner}: {my_account.balance}")
