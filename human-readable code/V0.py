# INTERNAL COMMENT
#
# "Works on my machine"
#
# 4.9 replaces the `2.0 * ... / 9.8` components of the normal equation

v = float(input("Launch velocity?"))
a = float(input("Launch angle?"))
import math
t = v * math.sin(a) / 4.9
f = float(input("Target distance?"))
o = t * v * math.cos(a) - f
print("Flight time:", t)
if math.fabs(o / f) < 2.0e-2:
    print("Hit.")
elif o < 0.0:
    print("Fell short.")
else:
    print("Went long.")
