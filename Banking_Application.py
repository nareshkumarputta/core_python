class Bank:
    def __init__(self, accno, pin, balance):
        self.accno = accno
        self.pin = pin
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your account XXXXX{self.accno %10000} has been credited with amount Rs.",amount)
        else:
            print("Invalid Amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Your account XXXXX{self.accno %10000} has been debited with amount Rs.",amount)
        else:
            if amount < self.balance:
                print("Insufficient Funds.")
            else:
                print("Invalid Amount.")
    def check_balance(self):
        print("Your current balance is : Rs.",self.balance)
acc1 = Bank(123403362, 4444, 100000)
acc2 = Bank(567800339, 9999, 1500)
acno = int(input("Enter your account number :"))
if acno == acc1.accno:
    pin = int(input("Enter your pin:"))
    if pin == acc1.pin:
        print("Login Successful!")
        while True:
            print("1.Deposit\n2.Withdraw\n3.Check Balance")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                amount = int(input("Enter the amount you want to deposit :"))
                acc1.deposit(amount)
            elif choice == 2:
                amount = int(input("Enter the amount you want to withdraw :"))
                acc1.withdraw(amount)
            elif choice == 3:
                acc1.check_balance()
            else:
                print("Invalid Choice")
                break
    else:
        print("Incorrect Pin")
elif acno == acc2.accno:
    pin = int(input("Enter your pin:"))
    if pin == acc2.pin:
        print("Login Successful!")
        while True:
            print("1. Deposit\n2.Withdraw\n3.Check Balance")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                amount = int(input("Enter the amount you want to deposit :"))
                acc2.deposit(amount)
            elif choice == 2:
                amount = int(input("Enter the amount you want to withdraw :"))
                acc2.withdraw(amount)
            elif choice == 3:
                acc2.check_balance()
            else:
                print("Invalid Choice")
                break
    else:
        print("Incorrect Pin")
else:
    print("Invalid Account Number")
