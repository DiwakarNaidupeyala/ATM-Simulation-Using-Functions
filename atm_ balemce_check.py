
balence=10000
def check_balance():
    print("balence",balence)
def deposit():
    global balence
    
    amount=int(input("enter deposited amount"))
    if amount<=0:
        print("enter positive values")
    else:
        balence+=amount
        print("available balence",balence)
def with_draw():
    global balence
    amount=int(input("enter withdraw amount"))
    if amount<=0:
        print("enter positive values")
    elif amount>balence:
        print("insufficient balence")
    else:
        balence-=amount
        print("available balence",balence)
def show_menu():
    print("1.checkbalence")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
while True:
    show_menu()   
    choice=int(input("enter your choice"))
    if choice==1:
        check_balance()
    elif choice==2:
        deposit()
    elif choice==3:
        with_draw()
    elif choice==4:
        print("exit")
        break
    else:
        print("out of range")
    



        
    
        
   
