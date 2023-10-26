import math
while True:
    op=input("plese choose operation:(+,-,*,/,etc.) or exit:")
    if op=="exit":
        break
    a=int(input("please enter a:"))
    b=int(input("please enter b:"))
    if op=="+":
        print(a+b)
    if op=="-":
        print(a-b)
    if op=="*":
        print(a*b)
    if op=="/" and b==0:
        print("try again")
    if op=="/"and b!=0:
        print(a/b)
    if op=="//":
        print(a//b)
    if op=="**":
        print(a**b)
    if op=="sqrt":
        print(math.sqrt(a),",",math.sqrt(b))
    if op=="sin":
        print(math.sin(math.radians(a)),math.sin(math.radians(b)))
    if op=="cos":
        print(math.cos(math.radians(a)),math.cos(math.radians(b)))
    if op=="tan":
        print(math.tan(math.radians(a)),math.tan(math.radians(b)))
    if op=="cot":
        print((math.sin(math.radians(a)))/(math.cos(math.radians(a))),(math.sin(math.radians(b)))/(math.cos(math.radians(b))))
    if op=="!":
        print(math.factorial(a),",",math.factorial(b))

