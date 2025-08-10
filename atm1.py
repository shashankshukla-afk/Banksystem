class bankaccount:
    def __init__ (self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        
    def deposit(self, amount):
        # balance badhao
        amount = float(input("Enter amount to deposit: ₹"))
        self.balance += amount
        print(f"Deposited ${amount}. New balance:${self.balance}")


    def withdraw(self, amount):
        # balance kam karo agar possible ho
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")


    def display(self):
        # details print karo
        print (f"Name = {self.name}")
        print (f"acc_no = {self.acc_no}")
        print (f"balance = {self.balance}")

e1 = bankaccount("rakash",12345,90000)


# Testing
e1.display()
e1.deposit(1)
e1.withdraw(1)
e1.display()


# Menu system
while True:
    print("\n----- ATM Menu -----")
    print("1. Display Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        e1.display()
    elif choice == "2":
        e1.deposit()
    elif choice == "3":
        e1.withdraw()
    elif choice == "4":
        print("Thank you for using ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")



