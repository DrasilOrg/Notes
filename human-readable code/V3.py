# ## [$V_3$: Layered Phases + Library, Program Split + Documentation: Deliverable, maintainable, short-living software](./V3.py)
#
# $V_3$ refines $V_2$ in two ways:
#
# 1. *Splitting off a library.* The program is split in two (within-file, via
#    `__name__` differentiation): an executable program and a library. The library
#    is meant to be production-ready, publishable with full coverage, extensive
#    documentation using conventional documentation software (`p[y]doc`).
# 2. *Creating documentation.* Not included here, but is expected to be in a
#    nearby `../SRS` folder, is Projectile's software requirements specification
#    that includes derivations for the formulas used in the code. Additionally, it
#    contains more background/context information about when the library should be
#    used (i.e., when the SRS is applicable).
#
# Overall, $V_3$ is meant to maintainable specialty software well-suited for a
# well-defined use-case. While not specifically intended to be publically
# published, it is only a short few steps away from being so: 
#
# 1. A design specification (at least a vague one).
# 2. Continuous integration scripts.
# 3. Testing scripts.
# 4. A `README` w/ usage examples.
# 5. Installation documentation.
# 6. License.

"""
PROJECTILE MOTION
  Samuel J. Crawford, Brooks MacLachlan, and W. Spencer Smith (2019)
                {craw.., machl.., smiths}@mcmaster.ca

Approximate whether a projectile hits a target.
"""

import math

#-------------------------------------------------------------------------------
# CALCULATION TOOLS
#
# Using kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
#
# Derived from <file://../SRS/Index.html#Sec:InstanceModels>.
#-------------------------------------------------------------------------------

def flight_time(v_launch, theta, g=9.8):
    """Calculate the projectile's total time in the air (s)

    Derived from <file://../SRS/Index.html#IM:flightDuration>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta (float): The launch angle in radians.
        g (float, optional): The acceleration due to gravity (m/s^2).
                             Defaults to 9.8 m/s^2.
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


def analyze_shot(v_launch, theta, p_target, g=9.8):
    """Determines the outcome of the shot after running calculations.

    Derived from <file://../CodeSpec/Index.html#NFR:Outputs>.

    Args:
        v_launch (float): The initial launch velocity in m/s.
        theta (float): The launch angle in radians.
        p_target (float): The target's distance in meters.
        g (float, optional): The acceleration due to gravity (m/s^2).
            Defaults to 9.8 m/s^2 (Earth approximation).

    Returns:
        tuple: A tuple containing the calculated flight time (s) and
            landing position (m) of the projectile.
    """
    assert p_target > 0.0, "Failed constraint: target > 0m away"
    
    t_flight = flight_time(v_launch, theta, g)
    p_land = landing_position(t_flight, v_launch, theta)

    return t_flight, p_land


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

    t_flight, p_land = analyze_shot(v_launch, theta, p_target)
