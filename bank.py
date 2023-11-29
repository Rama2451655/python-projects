class bank:
    Bank_name   ="SBI"
    Branch_name ="kadapa"
    IFSC        ="SBIN0000830"
    ROI         =0.06
    def __init__(self,Name,AccountNo,MobileNo,Bal,Pin):
        self.Name      =Name
        self.AccountNo =AccountNo
        self.MobileNo  =MobileNo
        self.Bal       =Bal
        self.Pin       =Pin
b1=bank("ramakrishna",42682466482,9846486647,47231,7678) 
@staticmethod
def validate():
    return int(input("enter 4 digit pin"))
def Deposit(self):
    if self.Pin==self.validate():
        amount=int(input("enter Amount:"))
        self.Bal+=amount
        print("amount deposited successfully")
    else:
        print("incorrect pin")
def withdraw(self):
    if self.Pin==self.validate():
        amount=int(input("enter Amount:"))
        if self.Bal>=amount:
            self.Bal-=amount
            print("amount debited successfully")
        else:
            print("incorrect pin")
    else:
            print("incorrect pin")
def checkBalance(self):
    if self.Pin==self.validate():
        print('{self.Bal}')
    else:
        print('incorrect pin')
@classmethod
def changeROI(cls):
    cls.ROI=float(input("enter ROI"))
    print("changed ROI successfully")
def changePin(self):
    if self.Pin==self.validate():
        pin1=int(input("enter new pin"))
        pin2=int(input("confirm new pin"))
        if pin1==pin2:
            self.Pin=pin1
        else:
            print("pin not matching")
    else:
        print("incorrect pin")
