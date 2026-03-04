"""name="shannu"
course="python"
#to add
print(name+" "+course)
#to access
print(name[0])
#to change
print("b" + name[1:])
#slicing
print(name[-6:])
print(name[-1])
print(name[-1:-7:-1])


#length of chrcater
name="codegnan"
len(name)
name.upper()
"""
"""
#password validation
pwd=input("Enter the password:")
if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("min 8 characters")


#usename gneeration#error

name=input("enter the name:")
dob=input("enter the dob[YYYY-MM-DD:]")
username=name[:2]+name[-2:]+dob[-2:]+dob[2:4]
print('f hi {name}your username: is{username}')  
         
 



data={
1:{'product':'bread',"price":200},
2:{'product':'cake',"price":400},    
3:{'product':'biscuit',"price":10},        
4:{'product':'salt',"price":50},
5:{'product':'soap',"price":50},
6:{'product':'tea powder',"price":70},
7:{'product':'eggs(12pcs)',"price":70},
8:{'product':'Rice',"price":100},
}
print('Index'.ljust(7,' '),'Product Name'. ljust(20,' '),'Price'.ljust(10,' '))
for i in data:
    print (str(i).ljust(7,' '),data[i]['product'].ljust(20,' '),str(data[i]['price']).ljust (10,''))

indexes =list (map (int, input ("Enter the indexes:").split()))
print ("Bill". center (30,'-'))
total_bill=0
for i in indexes:
    print (f'{data[i]["product"]}- ${data[i]["price"]}')
    total_bill+= data[i]["price"]
print (f"Your Bill: {total_bill}")

 """  
data = {
    1: {'product': 'bread', "price": 200},
    2: {'product': 'cake', "price": 400},
    3: {'product': 'biscuit', "price": 10},
    4: {'product': 'salt', "price": 50},
    5: {'product': 'soap', "price": 50},
    6: {'product': 'tea powder', "price": 70},
    7: {'product': 'eggs(12pcs)', "price": 70},
    8: {'product': 'Rice', "price": 100},
}

print('Index'.ljust(7), 'Product Name'.ljust(20), 'Price'.ljust(10))

for i in data:
    print(str(i).ljust(7),
          data[i]['product'].ljust(20),
          str(data[i]['price']).ljust(10))

indexes = list(map(int, input().split()))

print("Bill".center(30, '-'))

total_bill = 0
s = set()

for i in indexes:
    if i not in s:
        print(f'{data[i]["product"]} {data[i]["price"]}*{indexes.count(i)}={data[i]["price"]*indexes.count(i)}')
        total_bill += data[i]["price"] * indexes.count(i)
        s.add(i)

print(f"Your Bill: ${total_bill}")
































    

          
