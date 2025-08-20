# INTERNAL COMMENT
#
# "Works on my machine"
#
# `/ 4.9`` replaces `2.0 * ... / 9.8` in the formula for `t`

s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
t = s * math.sin(Θ) / 4.9
f = float(input("Target distance?"))
Δ = t * s * math.cos(Θ) - f
print("Flight time:", t)
if math.fabs(Δ / f) < 2.0e-2:
    print("Hit.")
elif Δ < 0.0:
    print("Fell short.")
else:
    print("Went long.")
