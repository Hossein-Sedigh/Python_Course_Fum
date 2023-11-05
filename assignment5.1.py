import random
list_lenght=int(input("please enter lenght number:"))
a=int(input("a:"))
b=int(input("b:"))
list=[]
for i in range(list_lenght):
    list.append(random.randint(a,b))
print(list)

