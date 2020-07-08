import random

class Bank:
    
    def __init__(self):      
        self.dict={}
    
    def create(self):
        balance=0
        iin = 400000_0000000000
        print("Your card has been created")
        print("Your card number:")
        j=random.sample(range(9999999999), 1)
        print(iin+j[0])
        print("Your card pin:")
        pin = random.sample(range(9999), 1)
        print(pin[0])
        a=iin+j[0]
        
        self.dict[a]={}
        self.dict[a]['pin']=pin[0]
        self.dict[a]['bal']=balance
        j.clear()
        pin.clear() 
    
    
    def logged(self,n,m):
        print("1. Create an account\n2. Log into account\n0. Exit")
        k=int(input())
        print()
        while(k != 0):
            if(k == 1):
                print()
                print("Balance",end="")
                print((self.dict[n]['bal']))
            elif(k == 2):             
                print('You have successfully logged out!')
                return "ok"
                break
            print()
            print("1. Create an account\n2. Log into account\n0. Exit")
        
            k=int(input())
        return "prob"
        
                
    def login(self):
        print("Enter your card number:")
        n = int(input())
    
        print("Enter your PIN:")
        m = int(input())
        
        if((n in self.dict.keys()) and (m == (self.dict[n]['pin']))):
            print()
            print("You have successfully logged in!")
            print()
            return self.logged(n,m)
   
        else:
            print()
            print("Wrong card number or PIN!")
                
print("1. Create an account\n2. Log into account\n0. Exit")
ch=int(input())
print()
ad=Bank()
while(ch != 0):
    if(ch == 1):
        ad.create()
    elif(ch == 2):
        if(ad.login() == "prob"):
            break
    print()
    print("1. Create an account\n2. Log into account\n0. Exit")
    ch=int(input())
print()
print("Bye!")
   
