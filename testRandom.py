import random

for x in range(0,1000,1):
    x = random.randrange(0,1000,1)

    print(x,end = "//")
    if x > 900:
        print("[poop]")
    else:
        print("-",end = "")