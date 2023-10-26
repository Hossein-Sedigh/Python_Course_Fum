import random
random_number=random.randint(1,100)
guess=0
while True:
    x=int(input("please enter x:"))
    if x<random_number:
        print("adad bozorgtari vared konid")
        guess+=1
    if x>random_number:
        print("adad koochektari vared konid")
        guess+=1
    if x==random_number:
        print("congragulation")
        guess+=1
        break
print({guess})