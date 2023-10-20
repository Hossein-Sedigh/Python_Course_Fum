a=int(input("a=:"))
b=int(input("b=:"))
c=int(input("c=:"))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a:
   print("ok, it is possible")
else:
    print("try again")
