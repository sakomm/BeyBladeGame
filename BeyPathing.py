# wait this is dumb the player will control it
import numpy as np
from matplotlib import pyplot as plt
import random # not random enough or maybe it is good enough idk
ArrX = []
Arry = []

for i in range(1,100,1):
    x = 1 + (random.random() * 1000)
    y = 1 + (random.random() * 1000)

    ArrX.append(x)
    Arry.append(y)

plt.plot(ArrX, Arry)

ArrX2 = []
ArrY2 = []

for i in range(1,100,1):
    x2 = 1 + (random.random() * 1000)
    y2 = 1 + (random.random() * 1000)

    ArrX2.append(x2)
    ArrY2.append(y2)

plt.plot(ArrX2, ArrY2,'r')
plt.show()
