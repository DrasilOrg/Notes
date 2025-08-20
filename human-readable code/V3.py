# INTERNAL COMMENT
#
# Straight Line version with:
# 1. Clarified units
# 2. Special constants in variables bundled in a class
# 3. New outputs: p_land and d_offset
# 4. Sanity constraints on inputs
# 5. Annotated variables
# 6. Code organization using language-specific features (functions, classes,
#    __name__)
# 7. Idiomatic header w/ license information
# 8. Backlinks to the SRS

"""
PROJECTILE MOTION
  Samuel J. Crawford, Brooks MacLachlan, and W. Spencer Smith (2019)

Approximate whether a projectile hits a target.


Copyright (c) 2019, Samuel J. Crawford, Brooks MacLachlan, and W. Spencer Smith.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
  1. ... (snip) ...
"""

import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

class Constants:
    """Physical and system-specific constants.
    
    See <file://../SRS/Index.html#Tab:Constants> for more information.
    """
    g = 9.8  # Gravity constant, conventional assumption: 9.8 m/s^2.
    epsilon = 2.0e-2  # A tolerance for hitting the target, 2% of the total distance.

#-------------------------------------------------------------------------------
# CALCULATION TOOLS
#
# Using kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
#-------------------------------------------------------------------------------

def calc_flight_time(v_launch, theta, g=Constants.g):
    """Calculate the projectile's total time in the air (s)
    
    Derived from <file://../SRS/Index.html#IM:flightDuration>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta_rad (float): The launch angle in radians.

    Returns:
        float: The total flight time in seconds.
    """
    return 2.0 * v_launch * math.sin(theta) / Constants.g


def calc_landing_position(v_launch, theta, g=Constants.g):
    """Calculates the projectile's landing distance from origin (m).

    Derived from <file://../SRS/Index.html#IM:landingPos>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta_rad (float): The launch angle in radians.

    Returns:
        float: The horizontal distance traveled in meters.
    """
    return calc_flight_time(v_launch, theta) * v_launch * math.cos(theta)


def analyze_shot(p_land, p_target, eps=Constants.epsilon):
    """Determines the outcome of the shot.

    Derived from <file://../CodeSpec/Index.html#NFR:Outputs>.

    Args:
        p_land (float): The projectile's calculated landing position in meters.
        p_target (float): The target's distance in meters.

    Returns:
        tuple[float, str]: A tuple containing the offset distance (m) and the
                           result message as a string.
    """
    offset = p_land - p_target
    relative_offset = math.fabs(offset / p_target)

    if relative_offset < eps:
        message = "The target was hit."
    elif offset < 0.0:
        message = "The projectile fell short."
    else:
        message = "The projectile went long."

    return offset, message


if __name__ == '__main__':
    #---------------------------------------------------------------------------
    # INPUTS
    #---------------------------------------------------------------------------

    v_launch = float(input("Launch velocity? (m/s)"))  # The initial velocity of the projectile.
    theta = float(input("Launch angle? (rad)"))  # The angle at which the projectile is launched.
    p_target = float(input("Distance to target? (m)"))  # The distance to the target.

    #---------------------------------------------------------------------------
    # INPUT CONSTRAINTS
    #---------------------------------------------------------------------------

    assert v_launch > 0.0, "Failed constraint: please provide positive velocity."
    assert 0.0 < theta and theta < math.pi / 2.0, "Failed constraint: 0 < theta < pi/2"
    assert p_target > 0.0, "Failed constraint: target > 0m away"

    #---------------------------------------------------------------------------
    # CALCULATIONS
    #---------------------------------------------------------------------------

    t_flight = calc_flight_time(v_launch, theta)
    p_land = calc_landing_position(v_launch, theta)
    d_offset, output_message = analyze_shot(p_land, p_target)

    #---------------------------------------------------------------------------
    # OUTPUTS
    #---------------------------------------------------------------------------

    print("Time in flight (s):", t_flight)
    print(f"Landed at {p_land}m ({d_offset}m away from target)")
    print(output_message)
