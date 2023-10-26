import random

tas_num = random.randint(1, 6)
print(tas_num)
if tas_num < 6:
    print("try again")
while tas_num == 6:
    for i in range(2):
        tas_num = random.randint(1, 6)
        print(tas_num)
