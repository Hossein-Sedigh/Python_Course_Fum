name=input("enter your name:")
Family=input("enter your family:")
a=int(input("enter your english score:"))
b=int(input("enter your math score:"))
c=int(input("enter your art score:"))
average=((a+b+c)/3)
print("your average:",average)
if average>=17:
    print("Great")
if 12<=average<17:
    print("Normal")
if average<12:
    print("Fail")