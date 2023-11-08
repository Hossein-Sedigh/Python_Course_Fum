m=int(input("enter m:"))
n=int(input("enter n:"))

for row in range(m):
    print()
    for col in range(n):
        if row%2==0:
            print("#","*",sep="",end=" ")
        if row%2!=0:
            print("*", "#", sep="", end=" ")
