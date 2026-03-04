"""#functions in python

def student_data(info):
    print(f'Name:{info[0]}')
    print(f'course:{info[1]}')
    print(f'Gra year:{info[2]}')
    print("--------END--------")

    


data=[['shannu','PFS','2026'],
['chakri','PFS','2026'],
['saaketh','PFS','2025'],
['zoroo','PFS','2026'],
      ]
      
for i in data:
    student_data(i)


#position
def display(uname,email,password):
    print(f'username:{uname}')
    print(f'email:{email}')
    print(f'password:{password}')
    print('\n\n')
    
display('shannu','shannu@124','12324')
display('shannu@124','shannu','12324')

#example
def results(python,java,aptitude,status='Absent'):
    print(f'python:{35}')
    print(f'java:{39}')
    print(f'aptitude:{20}')
    #default value agument
    print(f'status:{status}')
    print("\n\n")

results('python','java','aptitude')
print('\n')
#key-value agument
results(aptitude='',python='',java='')

 


def display(*names):
    for i in names:
        print(i)
        
    else:
        print("----------END OF LIST---------")
        
display("shannu")
display("shannu","saaketh")
display("shannu","saaketh","chakri")



#ATM MENU

balance = 0
history = []

# Deposit function
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    history.append(f"Deposited: ₹{amount}")
    print("Deposit successful!")

# Withdraw function
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        history.append(f"Withdrew: ₹{amount}")
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

# Check balance
def check_balance():
    print(f"Current balance: ₹{balance}")

# Transaction history
def show_history():
    print("Transaction History:")
    if not history:
        print("No transactions yet.")
    else:
        for h in history:
         print(h)
   """  
# ATM Menu

data = {
    123456 : {'pin':1234,'balance':5000,'history':[]},
    234561 : {'pin':2341,'balance':10000,'history':[]},
    345612 : {'pin':3423,'balance':7000,'history':[]}
}

def check_balance(acc):
    print(f"Your Balance Amount is ${data[acc]['balance']}")

def deposit(acc):
    amount = int(input("Enter the amount: "))
    data[acc]['balance']+=amount
    data[acc]['history'].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")

def withdraw(acc):
    amount = int(input("Enter the amount: "))
    if amount<=data[acc]['balance']:
        data[acc]['balance']-=amount
        data[acc]['history'].append(f"{amount} is Withdraw")
        print(f"{amount} is withdraw successfully")
    else:
        print("You don't have enough balance")
        
def setpin(acc):
    old_pin = int(input("Enter your current PIN: "))

    if old_pin == data[acc]['pin']:
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))

        if new_pin == confirm_pin:
            data[acc]['pin'] = new_pin
            data[acc]['history'].append("PIN changed successfully")
            print("---PIN updated successfully--- !!!")
        else:
            print("New PIN and Confirm PIN didn't match ")
    else:
        print("Incorrect current PIN ")




def view_history(acc):
    if  data[acc]['history']:
        print("-------Transaction History---------")
        for i in data[acc]['history']:
            print(i)
        else:
            print("--------End of history-------")
    else:
        print("No Transactions")

        
def menu():
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Set Pin')
    print('5.View Transactions')
    print('6.Exit\n')

print("Welcome to the ATM")

acc = int(input("Enter the account number: "))
pin = int(input("Enter the pin: "))

if acc in data and data[acc]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        ch = int(input("Enter the choice: "))
        if ch==1:
            check_balance(acc)
        elif ch==2:
            deposit(acc)
        elif ch==3:
            withdraw(acc)
        elif ch==4:
            setpin(acc)
        elif ch==5:
            view_history(acc)
        elif ch==6:
            print("Thankyou")
            break
else:
    print("Invalid Login. Try Again")

































































