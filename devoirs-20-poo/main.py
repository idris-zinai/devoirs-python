class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited to {self.owner}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn from {self.owner}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob", 50)

account1.deposit(50)
account1.withdraw(30)

account2.deposit(100)
account2.withdraw(200)

print(account1)
print(account2)