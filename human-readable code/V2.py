# INTERNAL COMMENT
#
# Straight Line version with:
# 1. Clarified units
# 2. Special constants in variables
# 3. New outputs: p_land and d_offset
# 4. Sanity constraints on inputs
# 5. Annotated variables
# 6. Organization by constants/inputs/constraints/calculations/outputs (#s for
#    borders)
# 7. Descriptive header

################################################################################
#
# PROJECTILE MOTION
#   Samuel J. Crawford, Brooks MacLachlan, and W. Spencer Smith (2019).
#                 {craw.., machl.., smiths}@mcmaster.ca
#
# Approximate whether a projectile hits a target.
#
################################################################################

import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8  # Gravity constant, conventional assumption: 9.8 m/s^2.
epsilon = 2.0e-2  # A tolerance for hitting the target, 2% of the total distance.

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

v_launch = float(input("Launch velocity? (m/s)"))  # The initial velocity of the projectile.
theta = float(input("Launch angle? (rad)"))  # The angle at which the projectile is launched.
p_target = float(input("Distance to target? (m)"))  # The distance to the target.

#-------------------------------------------------------------------------------
# VALIDATE INPUTS
#-------------------------------------------------------------------------------

assert v_launch > 0.0, "Failed constraint: please provide positive velocity."
assert 0.0 < theta and theta < math.pi / 2.0, "Failed constraint: 0 < theta < pi/2"
assert p_target > 0.0, "Failed constraint: target > 0m away"

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------

# Kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
t_flight = 2.0 * v_launch * math.sin(theta) / g  # Time projectile in motion 
p_land = t_flight * v_launch * math.cos(theta)  # Projectile landing position
d_offset = p_land - p_target  # Distance between the landing position and the target position

#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------

print("Time in flight (s):", t_flight)
print(f"Landed at {p_land}m ({d_offset}m away from target)")
if math.fabs(d_offset / p_target) < epsilon:
    print("The target was hit.")
elif d_offset < 0.0:
    print("The projectile fell short.")
else:
    print("The projectile went long.")
