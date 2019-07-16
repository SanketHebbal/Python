class BankAccount:
    ROI = 5

    def __init__(self,name,balance):
        self.Name = name
        self.Balance = balance

    def Display(self):
        print("\n{} has Balance {}\n".format(self.Name,self.Balance))

    def Deposit(self):
        amount = float(input("Enter the amount to be deposit ->"))
        self.Balance += amount
        self.Display()

    def Withdraw(self):
        
        amount = float(input("Enter the amount to be withdraw ->"))

        if(self.Balance < amount):
            print("Insufficient Balance !!!")
            return
        else:
            self.Balance -=amount

        self.Display()

    def CalculateInterest(self):
        interest = (self.Balance*BankAccount.ROI*1)/100
        print("Simple interest {}".format(interest))

def AcceptName():
    return input("Enter name ->")

def AcceptBalance():
    return float(input("Enter balance ->"))

obj1 = BankAccount(AcceptName(),AcceptBalance())
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
