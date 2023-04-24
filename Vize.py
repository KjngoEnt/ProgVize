import numpy as np
import matplotlib.pylab as plot
import math as m
import random as r

ANGLE = 30
C_HEIGHT = 24
G = 9.8
targetDistance = 20000+200*r.randint(-10, 10)
targetStart = targetDistance
targetEnd = targetDistance+1000+100*r.randint(-2, 2)
THETA = 30*m.pi/180
shotCount = 0
v = r.randint(330, 1800)

t = np.linspace(0, 300, num=1000)
while True:

    x1 = []
    y1 = []
    for i in t:
        x = ((v*i)*np.cos(THETA))
        y = ((v*i)*np.sin(THETA))-((0.5*G)*(i**2))
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0]
    for i in sorted(p, reverse=True):
        del x1[i]
        del y1[i]
    if x1[len(x1) - 1] <= targetEnd and x1[len(x1) - 1] >= targetStart:
        shotCount += 1
        break
    elif x1[len(x1) - 1] >= targetEnd:
        v = r.randint(330, v)
        shotCount += 1
        print("uzagina dustu")
    elif x1[len(x1) - 1] <= targetStart:
        v = r.randint(v, 1800)
        shotCount += 1
        print("onune dustu")

plot.plot(x1, y1)
print("Hedefi vurdun")
print(str(shotCount) +
      ".seferde vurus gerceklesmistir hedefi vurmak icin gerekli hiz " +
      str(v))
plot.show()
