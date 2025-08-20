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
                {craw.., machl.., smiths}@mcmaster.ca

Approximate whether a projectile hits a target.
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
    epsilon = 2.0  # A tolerance for hitting the target, 2% (of the total distance to the target).

#-------------------------------------------------------------------------------
# CALCULATION TOOLS
#
# Using kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
#-------------------------------------------------------------------------------

def flight_time(v_launch, theta, g=Constants.g):
    """Calculate the projectile's total time in the air (s)

    Derived from <file://../SRS/Index.html#IM:flightDuration>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta (float): The launch angle in radians.
        g (float, optional): The acceleration due to gravity (m/s^2).
                             Defaults to Constants.g.
    Returns:
        float: The total flight time in seconds.
    """
    assert v_launch > 0.0, "Failed constraint: please provide positive velocity."
    assert 0.0 < theta < math.pi / 2.0, "Failed constraint: 0 < theta < pi/2"
    assert g > 0.0, "Failed constraint: g must be positive."

    return 2.0 * v_launch * math.sin(theta) / g


def landing_position(flight_time, v_launch, theta):
    """Calculates the projectile's landing distance from origin (m).

    Derived from <file://../SRS/Index.html#IM:landingPos>.

    Args:
        flight_time (float): The total flight time in seconds.
        v_launch (float): The initial launch velocity in m/s.
        theta (float): The launch angle in radians.

    Returns:
        float: The horizontal distance traveled in meters.
    """
    assert flight_time >= 0.0, "Failed constraint: flight_time cannot be negative."
    assert v_launch > 0.0, "Failed constraint: please provide positive velocity."
    assert 0.0 < theta < math.pi / 2.0, "Failed constraint: 0 < theta < pi/2"

    return flight_time * v_launch * math.cos(theta)


def analyze_shot(v_launch, theta, p_target, g=Constants.g, eps=Constants.epsilon):
    """Determines the outcome of the shot after running calculations.

    Derived from <file://../CodeSpec/Index.html#NFR:Outputs>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta (float): The launch angle in radians.
        p_target (float): The target's distance in meters.
        g (float, optional): The acceleration due to gravity (m/s^2).
                             Defaults to Constants.g.
        eps (float, optional): The hit tolerance as a percentage (e.g., 2 for 2%).
                               Defaults to Constants.epsilon.

    Returns:
        tuple: A tuple containing the flight time (s), landing position (m),
               offset from target (m), and the outcome message (str).
    """
    assert p_target > 0.0, "Failed constraint: target > 0m away"
    assert 0 < eps < 100, "Failed constraint: epsilon must be between 0 and 100 %."
    
    t_flight = flight_time(v_launch, theta, g)
    p_land = landing_position(t_flight, v_launch, theta)

    offset = p_land - p_target
    relative_offset_pct = math.fabs(offset / p_target) * 100.0

    if relative_offset_pct < eps:
        message = "The target was hit."
    elif offset < 0.0:
        message = "The projectile fell short."
    else:
        message = "The projectile went long."

    return t_flight, p_land, offset, message


if __name__ == '__main__':
    #---------------------------------------------------------------------------
    # INPUTS
    #---------------------------------------------------------------------------

    v_launch = float(input("Launch velocity? (m/s)"))  # The initial velocity of the projectile.
    theta = float(input("Launch angle? (rad)"))  # The angle at which the projectile is launched.
    p_target = float(input("Distance to target? (m)"))  # The distance to the target.

    #---------------------------------------------------------------------------
    # CALCULATIONS & ANALYSIS
    #---------------------------------------------------------------------------

    t_flight, p_land, d_offset, output_message = analyze_shot(v_launch, theta, p_target)

    #---------------------------------------------------------------------------
    # OUTPUTS
    #---------------------------------------------------------------------------

    print("Time in flight (s):", t_flight)
    print(f"Landed at {p_land:.2f}m, {d_offset:.2f}m away from target")
    print(output_message)
