import random
a = random.random ()
a = round (a * 45)
while a == 0:
    a = random.random ()
    a = round (a * 45)
b = random.random ()
b = round (b * 45)
while b == (0 or a):
    b = random.random ()
    b = round (b * 45)
c = random.random ()
c = round (c * 45)
while c == (0 or a or b):
    c = random.random ()
    c = round (c * 45)
d = random.random ()
d = round (d * 45)
while d == (0 or a or b or c):
    d = random.random ()
    d = round (d * 45)
e = random.random ()
e = round (e * 45)
while e == (0 or a or b or c or d):
    e = random.random ()
    e = round (e * 45)
f = random.random ()
f = round (f * 45)
while f == (0 or a or b or c or d or e):
    f = random.random ()
    f = round (f * 45)
print (a, b, c, d, e, f)
#ich glaube es geht kürzer auch
