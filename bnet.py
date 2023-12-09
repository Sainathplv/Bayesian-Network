from bays import bays
from sys import argv

Gvalue = False
s1 = []
s2 = []

for i in argv:
    if i == "given":
        Gvalue = True
    s2.append(i)
    if Gvalue:
        s1.append(i)

bnet = bays()

if not s2:
    print("Query String is INVALID")
else:
    a = bnet.nValue(bnet.gtValue(s2))
    if s1:
        b = bnet.nValue(bnet.gtValue(s1))
    else:
        b = 1
    print("Probability = %.10f" % (a / b))

