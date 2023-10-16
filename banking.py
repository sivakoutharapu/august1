class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
        
    def menu(self):
        while True:
            print("CREATE PIN    Enter- 1:")
            print("DEPOSIT       Enter- 2:")
            print("WITHDRAW      Enter- 3:")
            print("CHECK BALANCE Enter- 4:")
            print("EXIT PROGRAM  Enter- 5:")
            user_input=input("CHOOSE ONE (1/2/3/4/5): ")
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposite()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
                print("check balance")
            else:
                print("exit program, Bye!!!")
                break
        
    def create_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully")
    def deposite(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to deposite"))
            self.balance=self.balance+amount
            print("deposite successfully")
        else:
            print("invalid pin")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount to withdraw"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("succesfully withdraw")
            else:
                print("insufficient balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        
        
Atm()
        
        
        
        
        
        
        
        
        
        
        