class ATM(object):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def setbalance(self,b):
        self.b=b
        self.balance=b
    def getname(self):
        return self.name
    def getbalance(self):
        return self.balance
    def deposit(self,bal):
        self.bal=bal
        self.balance=balance+bal
    def withdraw(self,w):
        self.w=w
        if(self.w<balance):
            self.balance=balance-w
        elif(self.w==balance):
            self.balance=balance-w
        else:
            print("Balance is less than withdraw")
    
name =str(input("Enter the name :")) 
balance =int(input("Enter the initial balance :"))
while(balance<=0):
    print("you Enter invalid balance")
    balance =int(input("Enter the balance again :"))
obj=ATM(name,balance)
print("Name is :",obj.getname())
num=0
while(num<4):
    
    print("For check balance enter 1 :")
    print("For deposit money enter 2 :")
    print("For withraw money enter 3 :")
    print("For exit program enter 4 or 4> :")
    num=int(input())
    if(num==1):
        if(obj.balance==0):
            print("Current balance is zero initial it first ")
            b=int(input("Enter the balance :"))
            while(b<=0):
                print("you Enter invalid balance")
                b =int(input("Enter the balance again :"))
            obj.setbalance(b)
            print("Current balance is :",obj.getbalance())
        else:
            print("Current balance is :",obj.getbalance())
    elif(num==2):
        d=int(input("Enter the money you want to deposit :"))
        if(d>=0):
            obj.deposit(d)
        else:
            print("Invalid input")
    elif(num==3):
        W = int(input("Enter the money you want to withdraw :"))
        obj.withdraw(W)
