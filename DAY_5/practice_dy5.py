"""
#FORLOOP

bikes=["triumph","BMW","kawasaki","jawa"]
for bikes in bikes:
    print(f'{bikes}-GO FOR A RIDE')


 # for loop TUPLE of items
sizes=('x','m','L','XXL','XL')
for s in sizes:
    print(f'___{s}___')



#for loop SET of followers
    
cars={"hyundai","maruti","BMW","mustang"}
for cars in cars:
    print(f'{cars}-take a look')



#for loop DICT
    
studentdata = {
    'shannu': ['java','python','sql'],
    'saketh': ['java','c++','sql'],
    'nikhil': ['java','c','sql']
}

for i in studentdata:
    print(f"{i} : {studentdata[i]}")
    print()

   
#STRING for loop
    
s="shannu goud"
for i in s:
    print(i)

#RANGE for loop
#range(start,stop+1,step)=range(0,n,1)
n=int(input("enter the table:"))
print(n"table")      
for i in range(1,11):
    print('f{n}*,i,"=",n*i')
    
for i in range(1,11):
    print(i)
   
#BREAK
    
for i in range(1,10):
  if i==6:
      break
  print(i)
  
#while loop
  
i=1
while i<=10:
  print(i)
  i=i+1


moves=15
winning_point = int(input("tell mw how many moves is required:"))
while moves>=1:
  if 15 - winning_point==moves:
    print("you won the game")
    break
  print(f'{moves} are left')
  moves=moves-1
else:
  print("GAME OVER")
"""

























