"""#simple-if
temp=90
if temp>100:
    print("fever")"""
"""
temp=90
if temp>100:
    print("fever")
else:
    print("normal temp")"""
"""


#if-else

bikes=[" triumph ","bMW" ,"RE","splendor"]
check=input("enter the bike name:")
if check in bikes:
    
    print(f'{check} is found\n"go for a ride')
else:
    print(f'{check}is not found\nride another bike')
    
"""



"""
#if-elif
a=90
b=100
c=140
if a>b and a>c:
    print("a got 1st rank")
elif b>a and b>c:
    
    print("b got 1st rank")
else:
    print("c got 1st rank")
"""


#nested if
bike = input("Do you have a bike? (yes/no): ").lower()

if bike == "yes":
    age = int(input("Enter age: "))
    
    if age >= 18:
        license = input("Do you have license? (yes/no): ").lower()
        
        if license == "yes":
            helmet = input("Do you have helmet? (yes/no): ").lower()
            
            if helmet == "yes":
                print("You can go for a ride")
            else:
                print("Get a helmet first")
        else:
            print("Get a license")
    else:
        print("You are underage")
else:
    print("Go get a bike first")

                

    





