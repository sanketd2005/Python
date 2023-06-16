# withdraw :
def withdraw():
    global opbal
    global msg
    msg = "Enter PIN"
    global pin2
    p=int(input(msg))
    if p==pin2 :
        amt=int(input("Enter Amount to be Withdraw :"))
        if amt > opbal :
            print("Insufficient Fund ".center(100,"="))
            print("Available Balance :Rs.{}/-".format(opbal).center(100,"-"))
        else:
            opbal -= amt
            print("Withdraw of {} is Successful ".format(amt))
            print("Available Balnace :Rs.{}/-".format(opbal))
    print("=".center(100,"="))
    
# Deposit :
def deposite():
    global opbal
    
    p=int(input(msg))
    if p==pin2 :
        depamt = int(input("Enter Amount to be Deposited :"))
        opbal += depamt
        print("Rs.{}/- Deposited Successfully !".format(depamt).center(100))
        print("Available Balance :Rs.{}/-".format(opbal).center(100))
    print("=".center(100,"="))   
    
# check balance :
def check_balance():
    p=int(input(msg))
    if p==pin2:
        print(name)
        print("Account Balance :Rs.{}/-".format(opbal).center(100))
    print("=".center(100,"="))
    
# Login :
def login():
    global pin1 
    global pin2 
    pin1 = int(input("Enter PIN :"))
    pin2 = int(input("Confirm PIN :"))
    
# choice :
def choice():
    print("MENU".center(100,"-"))
    print("1.Withdraw :")
    print("2.Deposit :")
    print("3.Check Balance :")
    print("4.Exit :")
    print("".center(100,"-"))

# function called /main() 
login()
global pin1 
if pin1 == pin2:
    name = input("Enter Name : ")
    opbal = int(input("Enter A/c opening Balance :"))
    while True:
        choice()
        ch = int(input("Enter Choice :"))
        if (ch==1):
            withdraw()
        elif (ch==2):
            deposite()
        elif (ch==3):
            check_balance()
        elif (ch==4) :
            break
        else :
            print("invalid Input ")
            print("=".center(100,"="))
    print("Thank you ")
    print("=".center(100,"="))