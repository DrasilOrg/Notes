# INTERNAL COMMENT
#
# Straight Line version with:
# 1. Clarified units
# 2. Special constants in variables
# 3. New outputs: p_land and d_offset
# 4. Sanity constraints on inputs

v_launch = float(input("Launch velocity? (m/s)"))
assert v_launch > 0.0, "Failed constraint: please provide positive velocity."
theta = float(input("Launch angle? (rad)"))
import math
assert 0.0 < theta and theta < math.pi / 2.0, "Failed constraint: 0 < theta < pi/2"

g = 9.8 # gravity, m/s^2
t_flight = 2.0 * v_launch * math.sin(theta) / g
p_land = t_flight * v_launch * math.cos(theta)

p_target = float(input("Distance to target? (m)"))
assert p_target > 0.0, "Failed constraint: target > 0m away"

d_offset = p_land - p_target

print("Time in flight (s):", t_flight)
print(f"Landed at {p_land}m ({d_offset}m away from target)")
epsilon = 2.0e-2 # % of total distance to target
if math.fabs(d_offset / p_target) < epsilon:
    print("The target was hit.")
elif d_offset < 0.0:
    print("The projectile fell short.")
else:
    print("The projectile went long.")
