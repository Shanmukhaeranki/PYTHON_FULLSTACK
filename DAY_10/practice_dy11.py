
"""
#Square Pattern
n=5
for i in range(n):    
    for j in range(n):
        print("*", end=" ")
    print()
print("\n")

#Right Triangle (Increasing)
n=5
for i in range(1,n+1):
    print("* "*i )

print("\n")



#Right Triangle (Decreasing)
n=5
for i in range(n,0,-1):
    print("* "*i)


#pyramid pattern
n=5
for i in range(n):
    print(' '*(n-i-1)+"* "*(i+1))


# reverse pyramid pattern
n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)


#diamond pattrn
n=5
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

name="SHANNU"
for i in range(len(name)):
    print(" ".join(name[:i+1]))
"""










