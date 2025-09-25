##### $V_?$: $\bot$

A developer-hostile program. Prompts (without notification) for 2 inputs and uses them at usage site (i.e., no caching). Does not indicate which prompt is for which `float(input())`.

```python
import math
print(float(input()) ** 2 * math.sin(2 * float(input())) / 9.8)
```

##### $V_?$: Removing simplification: $2\sin{(a)}\cos{(a)}=\sin{(2a)}$

To obtain the one previous, I removed flight time output, inlined its expression into landing position, and removed the offset output and offset message output. What's left is this: landing position. One of the final expression simplifications permitted after inlining expressions was the above trigonometric formula. With the simplification removed, $\theta$ is used twice, but the configuration remains: no caching.

```python
import math
print(float(input()) ** 2 * math.sin(float(input())) * math.cos(float(input())) / 4.9)
```

##### $V_?$: Introduce simple inputs caching policy: strictly don't ask twice.

The new caching policy is to only cache if the variable needs to be used more than once.

```python
import math
Θ = float(input())
print(float(input()) ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9)
```

##### $V_?$: Input prompt messages

The `float(input())`s are a bit too rough to work with. Giving prompt messages, albeit terse ones, are helpful.

```python
import math
Θ = float(input("Angle?"))
print(float(input("Velocity?")) ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9)
```

##### $V_?$: Sensible input prompt messages

Just noting what the variables mean give the reader a bit more information about the relationship between the two variables.

```python
import math
Θ = float(input("Launch angle?"))
print(float(input("Launch velocity?")) ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9)
```

##### $V_?$: Strict input value caching policy

Slightly more readable code.

```python
s = float(input("Launch velocity?"))
import math
Θ = float(input("Launch angle?"))
print(s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9)
```

Note that `sin` appears before $\theta$ but after `s`, so we generate `s` input reading first.
##### $V_?$: Move landing position expression to variable.

```python
s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
pl = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9
print("Landing position:", pl)
```

Note that I intentionally use an odd symbol for "landing position:" `pl`.
##### $V_?$:  Introduce a new variable: landing distance to target

I will assume that the policy of caching expressions applies to all input and output variables. Not necessarily intermediate variables, which is not directly highlighted through this snippet.

```python
s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
pl = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9
print("Landing position:", pl)
pt = float(input("Target distance?"))
off = pl - pt
print("Landing distance to target:", off)
```

##### $V_?$:  Designate "flight time" to be an output variable

With flight time designated as an output variable (or alternatively because it will be used more once), it is cached in a variable before being output.

```python
s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
t = s * math.sin(Θ) / 4.9
print("Flight time:", t)
pl = s * t * math.cos(Θ)
print("Landing position:", pl)
pt = float(input("Target distance?"))
off = pl - pt
print("Landing distance to target:", off)
```

##### $V_?$:  Create a new output variable: a 'hit or not' message

```python
s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
t = s * math.sin(Θ) / 4.9
print("Flight time:", t)
pl = s * t * math.cos(Θ)
print("Landing position:", pl)
pt = float(input("Target distance?"))
off = pl - pt
print("Landing distance to target:", off)
if math.fabs(off / pt) < 2.0e-2:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  Introduce a whitespace policy: break code by output variables

```python
s = float(input("Launch velocity?"))
Θ = float(input("Launch angle?"))
import math
t = s * math.sin(Θ) / 4.9
print("Flight time:", t)

pl = s * t * math.cos(Θ)
print("Landing position:", pl)

pt = float(input("Target distance?"))
off = pl - pt
print("Landing distance to target:", off)

if math.fabs(off / pt) < 2.0e-2:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  Impose sanity constraints on inputs

```python
s = float(input("Launch velocity?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle?"))
import math
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
t = s * math.sin(Θ) / 4.9
print("Flight time:", t)

pl = s * t * math.cos(Θ)
print("Landing position:", pl)

pt = float(input("Target distance?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
print("Landing distance to target:", off)

if math.fabs(off / pt) < 2.0e-2:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  No constant folding (2 * ... / 9.8  <~~ ... / 4.9)

```python
s = float(input("Launch velocity?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle?"))
import math
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
t = 2 * s * math.sin(Θ) / 9.8
print("Flight time:", t)

pl = s * t * math.cos(Θ)
print("Landing position:", pl)

pt = float(input("Target distance?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
print("Landing distance to target:", off)

if math.fabs(off / pt) < 2.0e-2:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  "Prominent" (for lack of better words) constants to variables

```python
s = float(input("Launch velocity?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle?"))
import math
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
g = 9.8
t = 2 * s * math.sin(Θ) / g
print("Flight time:", t)

pl = s * t * math.cos(Θ)
print("Landing position:", pl)

pt = float(input("Target distance?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
print("Landing distance to target:", off)

e = 2.0e-2
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  Units captured in comments for intermediate variables and in input/output messages else

```python
s = float(input("Launch velocity (m/s)?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle (rad)?"))
import math
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
g = 9.8 # m/s^2
t = 2 * s * math.sin(Θ) / g
print("Flight time (s):", t)

pl = s * t * math.cos(Θ)
print("Landing position (m):", pl)

pt = float(input("Target distance (m)?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
print("Landing distance to target:", off)

e = 2.0e-2 # distance to target as a percentage of initial target distance
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  New code flow policy: Output variables grouped together, last

```python
s = float(input("Launch velocity (m/s)?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle (rad)?"))
import math
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
g = 9.8 # m/s^2
t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
pt = float(input("Target distance (m)?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
e = 2.0e-2 # distance to target as a percentage of initial target distance

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  New code flow policy: Imports first

```python
import math

s = float(input("Launch velocity (m/s)?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle (rad)?"))
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
g = 9.8 # m/s^2
t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
pt = float(input("Target distance (m)?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt
e = 2.0e-2 # distance to target as a percentage of initial target distance

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  New code flow policy: Constants declared immediately after imports

```python
import math

g = 9.8 # m/s^2
e = 2.0e-2 # distance to target as a percentage of initial target distance

s = float(input("Launch velocity (m/s)?"))
assert s > 0.0, "Velocity > 0.0"
Θ = float(input("Launch angle (rad)?"))
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
pt = float(input("Target distance (m)?"))
assert pt > 0.0, "pt > 0.0"
off = pl - pt

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```


##### $V_?$:  New code flow policy: Inputs grouped together (constraints don't follow)

```python
import math

g = 9.8 # m/s^2
e = 2.0e-2 # distance to target as a percentage of initial target distance

s = float(input("Launch velocity (m/s)?"))
Θ = float(input("Launch angle (rad)?"))
pt = float(input("Target distance (m)?"))

assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
assert pt > 0.0, "pt > 0.0"
off = pl - pt

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```


##### $V_?$:  New code flow policy: Input constraints grouped together

```python
import math

g = 9.8 # m/s^2
e = 2.0e-2 # distance to target as a percentage of initial target distance

s = float(input("Launch velocity (m/s)?"))
Θ = float(input("Launch angle (rad)?"))
pt = float(input("Target distance (m)?"))

assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
assert pt > 0.0, "pt > 0.0"

t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
off = pl - pt

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  Comment-based headers for grouped code

```python
# Imports
import math

# Constants
g = 9.8 # m/s^2
e = 2.0e-2 # distance to target as a percentage of initial target distance

# Inputs
s = float(input("Launch velocity (m/s)?"))
Θ = float(input("Launch angle (rad)?"))
pt = float(input("Target distance (m)?"))

# Verify inputs
assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
assert pt > 0.0, "pt > 0.0"

# Calculations
t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
off = pl - pt

# Outputs
print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  More prominent comment-based headers for grouped code, removing that for "imports"

```python
import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8 # m/s^2
e = 2.0e-2 # distance to target as a percentage of initial target distance

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

s = float(input("Launch velocity (m/s)?"))
Θ = float(input("Launch angle (rad)?"))
pt = float(input("Target distance (m)?"))

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
assert pt > 0.0, "pt > 0.0"

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------

t = 2 * s * math.sin(Θ) / g
pl = s * t * math.cos(Θ)
off = pl - pt

#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  More comments about variables and calculations (developer-friendliness)

```python
import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8  # Gravity constant, conventional assumption: 9.8 m/s^2.
e = 2.0e-2  # A tolerance for hitting the target, 2% of the distance from the launcher to the target.

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

s = float(input("Launch velocity (m/s)?"))  # The initial velocity of the projectile.
Θ = float(input("Launch angle (rad)?"))  # The angle at which the projectile is launched.
pt = float(input("Target distance (m)?"))  # The distance to the target.

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
assert pt > 0.0, "pt > 0.0"

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------

# Kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
t = 2 * s * math.sin(Θ) / g  # Time projectile in motion
pl = s * t * math.cos(Θ)  # Projectile landing position
off = pl - pt  # Distance between the landing position and the target position

#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```


##### $V_?$:  Program metainformation introduced in header

```python
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
e = 2.0e-2  # A tolerance for hitting the target, 2% of the distance from the launcher to the target.

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

s = float(input("Launch velocity (m/s)?"))  # The initial velocity of the projectile.
Θ = float(input("Launch angle (rad)?"))  # The angle at which the projectile is launched.
pt = float(input("Target distance (m)?"))  # The distance to the target.

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

assert s > 0.0, "Velocity > 0.0"
assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
assert pt > 0.0, "pt > 0.0"

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------

# Kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
t = 2 * s * math.sin(Θ) / g  # Time projectile in motion
pl = s * t * math.cos(Θ)  # Projectile landing position
off = pl - pt  # Distance between the landing position and the target position

#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------

print("Flight time (s):", t)
print("Landing position (m):", pl)
print("Landing distance to target:", off)
if math.fabs(off / pt) < e:
    print("Hit.")
elif off < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```

##### $V_?$:  Clearer variable names

```python
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
tolerance = 2.0e-2  # A tolerance for hitting the target, 2% of the distance from the launcher to the target.

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

v_launch = float(input("Launch velocity (m/s)?"))  # The initial velocity of the projectile.
angle_launch = float(input("Launch angle (rad)?"))  # The angle at which the projectile is launched.
target_distance = float(input("Target distance (m)?"))  # The distance to the target.

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

assert v_launch > 0.0, "Velocity > 0.0"
assert 0.0 < angle_launch and angle_launch < math.pi / 2.0, "0.0 < Θ < π/2"
assert target_distance > 0.0, "Target > 0.0"

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------

# Kinematic model of projectile motion assuming constant gravity, no air
# resistance, and point mass.
flight_time = 2 * v_launch * math.sin(angle_launch) / g  # Time projectile in motion
landing_position = v_launch * flight_time * math.cos(angle_launch)  # Projectile landing position
offset = landing_position - target_distance  # Distance between the landing position and the target position

#-------------------------------------------------------------------------------
# OUTPUTS
#-------------------------------------------------------------------------------

print("Flight time (s):", flight_time)
print("Landing position (m):", landing_position)
print("Landing distance to target:", offset)
if math.fabs(offset / landing_position) < tolerance:
    print("Hit.")
elif offset < 0.0:
    print("Fell short.")
else:
    print("Went long.")
```


