class Atm(object):
    def __init__(self,cardNumber,pinCode):
        self.cardNumber = input("Enter your Card Number")
        self.pinCode = input("Enter your Pin Code")

    def start(self):
        print("started")

a = 1000

def cashWithDrawal():
    #for deposit enter negative value i.e- -n , -109 etc.
    num = int(input("How much money you want to deposit or credit?"))
    value = 0
 
    if(num == value):
        a + 0
    
    if(num > value):
        a + num
    
    if(num < value):
        a + num

    if(num > 1000):
        print("Insufficient Balance")
    else:
        print("balance:",a + num)

def option():
    Option = input("what u want cashWithDrawal or balanceEnquiry")

    if(Option == "cashWithDrawal"):
        cashWithDrawal()
        print("Have a good day")

atm1 = Atm('cardNumber','pinCode')
print("Your card Number:"+atm1.cardNumber,",","Your pin code:"+atm1.pinCode)

option()
