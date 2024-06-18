from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
#hは幅 kは個数
import math
h=(math.pi/2)/100
k=1 
#Sは全体の面積
S=0
#s="k個目の台形の面積"
while k<=100:
    s=(h/2)*((sin((k-1)*h))+(sin(k*h)))
    S +=s
    k += 1
print(S)