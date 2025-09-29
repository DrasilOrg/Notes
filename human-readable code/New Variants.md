Hard-coded inputs:

* Launch velocity: $17~m/s$
* Angle: $\frac{\pi}{4}~rad$

## 007: $\bot$

A developer-hostile program. Prompts (without notification) for 2 inputs and uses them at usage site (i.e., no caching). Does not indicate which prompt is for which `float(input())`.

```python
import math
d = 17.0 ** 2 * math.sin(math.pi / 2) / 9.8
```

## Offense: Removing simplification: $2\sin{(a)}\cos{(a)}=\sin{(2a)}$

To obtain the one previous, I removed flight time output and inlined its expression into landing positiont. What's left is this: landing position. One of the final expression simplifications permitted after inlining expressions was the above trigonometric formula. With the simplification removed, $\theta$ is used twice, but the configuration remains: no caching.

```python
import math
d = 17.0 ** 2 * math.sin(math.pi / 4) * math.cos(math.pi / 4) / 4.9
```

## Octagon: Introduce simple inputs caching policy: don't inline repeated variable use

The new caching policy is to only cache if the variable needs to be used more than once.

```python
import math
Θ = math.pi / 4
d = 17.0 ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9
```

## Glider: Strict input value caching policy

Slightly more readable code.

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
d = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9
```

**Note**: `sin` appears before $\theta$ and after `s` in the `print` statement, so we generate `s` input assignment first, and then import `math`. The order of steps is approximately left-to-right including only what is strictly necessary above any particular step to reach the final output variable calculation.

## SuperBowl: Rename `d` to `pl`

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
pl = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9
```

## Crossroads: Add comment explaining what `d` is

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
pl = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9  # Landing position
```

## Ricochet: Introduce a new variable: flight time

I will assume that the policy of caching expressions applies to all input and output variables. Not necessarily intermediate variables, which is not directly highlighted through this snippet.

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
pl = s ** 2 * math.sin(Θ) * math.cos(Θ) / 4.9  # Landing position
```

## Commander: Designate "flight time" to be an output variable

With flight time designated as an output variable (or alternatively because it will be used more once), it is cached in a variable before being output.

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
t = s * math.sin(Θ) / 4.9  # Flight time
pl = s * t * math.cos(Θ)  # Landing position
```

## Blockade: Introduce a whitespace policy: break code by key variables of interest (i.e., "outputs")

```python
s = 17.0  # Launch velocity
import math
Θ = math.pi / 4  # Launch angle
t = s * math.sin(Θ) / 4.9  # Flight time

pl = s * t * math.cos(Θ)  # Landing position
```

## Invader: Introduce function for algorithm reuse

```python
def calc(s, Θ):
    # s: Launch velocity
    # Θ: Launch angle
    import math
    t = s * math.sin(Θ) / 4.9  # Flight time

    pl = s * t * math.cos(Θ)  # Landing position

    return (t, pl)


import math
t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Alert: Switch to [Google DocString Format](https://google.github.io/styleguide/pyguide.html) ([example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)) for function comments.

```python
def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    import math
    t = s * math.sin(Θ) / 4.9

    pl = s * t * math.cos(Θ)

    return (t, pl)


import math
t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Focus: De-duplicate imports

Unfortunately, Python's required 2 empty lines before/after function definitions become empty space spam in this document.

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    t = s * math.sin(Θ) / 4.9

    pl = s * t * math.cos(Θ)

    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Xenon: Don't break blocks by "output" variable calculations

I say "output" but I really mean "key variables of interest."

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    t = s * math.sin(Θ) / 4.9
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Genesis: Impose soft sanity constraints on inputs

Soft because `assert` is disableable by passing `-O` to Python. Note that the constraints are intermixed with the steps (only executed just before first use of a variable, same lazy policy).

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """

    assert s > 0.0, "Velocity > 0.0"
    assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"
    t = s * math.sin(Θ) / 4.9
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Backhander: New code policy: input value assertions grouped together in function blocks

Soft because `assert` is disableable by passing `-O` to Python.

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    assert s > 0.0, "Velocity > 0.0"
    assert 0.0 < Θ and Θ < math.pi / 2.0, "0.0 < Θ < π/2"

    t = s * math.sin(Θ) / 4.9
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Scrappy: Friendlier assertion messages

Soft because `assert` is disableable by passing `-O` to Python.

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    assert s > 0.0, "Velocity must be greater 0.0."
    assert 0.0 < Θ and Θ < math.pi / 2.0, "Launch angle must be within (0, pi/2)"

    t = s * math.sin(Θ) / 4.9
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Vicinity: Switch to hard sanity constraints (written in the negative)

Note that single-line blocks use the compressed Python block style.

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    t = s * math.sin(Θ) / 4.9
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Universe: No constant folding (`... / 4.9` ~~> `2 * ... / 9.8`)

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    t = 2 * s * math.sin(Θ) / 9.8
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Torch: "Prominent" (for lack of better words) constants to variables

```python
import math


def calc(s, Θ):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    g = 9.8  # Gravity constant
    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Edge: Move constants to optional function inputs

```python
import math


def calc(s, Θ, g=9.8):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle
        g (optional): Gravity constant

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Mad Hatter: Impose constraints on optional inputs

```python
import math


def calc(s, Θ, g=9.8):
    """
    Args:
        s: Launch velocity
        Θ: Launch angle
        g (optional): Gravity constant

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Foray: Add function description to docstring

Note Google DocString format dictates hard wrapping docstrings at character 72.

```python
import math


def calc(s, Θ, g=9.8):
    """Calculates a projectile's landing position and flight time given an
    initial launch velocity and launch angle.

    Args:
        s: Launch velocity
        Θ: Launch angle
        g (optional): Gravity constant

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Boxer: Clarify `pt`'s description

```python
import math


def calc(s, Θ, g=9.8):
    """Calculates a projectile's landing position and flight time given an
    initial launch velocity and launch angle.

    Args:
        s: Launch velocity
        Θ: Launch angle
        g (optional): Gravity constant

    Returns:
        t: Flight time
        pl: Landing position
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Pinball: Include unit information in docstring's Args/Returns sections

```python
import math


def calc(s, Θ, g=9.8):
    """Calculates a projectile's landing position and flight time given an
    initial launch velocity and launch angle.

    Args:
        s: Launch velocity (m)
        Θ: Launch angle (rad)
        g (optional): Gravity constant (m/s)

    Returns:
        t: Flight time (s)
        pl: Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Omega: Include unit information in docstring's function description

```python
import math


def calc(s, Θ, g=9.8):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s: Launch velocity (m)
        Θ: Launch angle (rad)
        g (optional): Gravity constant (m/s)

    Returns:
        t: Flight time (s)
        pl: Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Sunset: Include type information in docstring

```python
import math


def calc(s, Θ, g=9.8):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s (float): Launch velocity (m)
        Θ (float): Launch angle (rad)
        g (float, optional): Gravity constant (m/s)

    Returns:
        t (float): Flight time (s)
        pl (float): Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Steamroller: Add type hints on function inputs

```python
import math


def calc(s: float, Θ: float, g: float = 9.8):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s (float): Launch velocity (m)
        Θ (float): Launch angle (rad)
        g (float, optional): Gravity constant (m/s)

    Returns:
        t (float): Flight time (s)
        pl (float): Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Volcano: Add type hints on function outputs

```python
import math


def calc(s: float, Θ: float, float, g: float = 9.8) -> (float, float):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s (float): Launch velocity (m)
        Θ (float): Launch angle (rad)
        g (float, optional): Gravity constant (m/s)

    Returns:
        t (float): Flight time (s)
        pl (float): Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")
    if g <= 0.0: raise ValueError("Gravity constant must be strictly positive.")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Pinnacle: Move constants to global variables

This maintains the previous variable description/comment scheme. Additionally, because it is now presumed to be an immutable "constant," we remove the assertion in `calc`.

```python
import math

g = 9.8  # Gravity constant, m/s


def calc(s: float, Θ: float) -> (float, float):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s (float): Launch velocity (m)
        Θ (float): Launch angle (rad)

    Returns:
        t (float): Flight time (s)
        pl (float): Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Starlight: Introduce simple program metainformation at top of file

This is a "uniquely Python" [style](https://epydoc.sourceforge.net/manual-fields.html#module-metadata-variables).

```python
"""PROJECTILE MOTION

Approximate simple projectile motion.
"""
__authors__ = ["Samuel J. Crawford", "Brooks MacLachlan", "W. Spencer Smith"]
__contact__ = "{craw.., machl.., smiths}@mcmaster.ca"
__date__ = "January 1st, 2019"
__license__ = "GPLv3-or-later"

import math

g = 9.8  # Gravity constant, m/s


def calc(s: float, Θ: float) -> (float, float):
    """Calculates a projectile's landing position (m) and flight time (s)
    given an initial launch velocity (m/s) and launch angle (rad) of the
    projectile from a launcher on ground level.

    Args:
        s (float): Launch velocity (m)
        Θ (float): Launch angle (rad)

    Returns:
        t (float): Flight time (s)
        pl (float): Landing position (m)
    """
    if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
    if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

    t = 2 * s * math.sin(Θ) / g
    pl = s * t * math.cos(Θ)
    return (t, pl)


t, pl = calc(17.0, math.pi / 4)  # (Flight time, Landing position)
```

## Blockade: Comment-based headers for grouped code

There is a chasm of variations between the variation just before the introduction of functions and this one. This variation does not go to a function-based grouping, but simple comment-based organization within file (impromptu abstraction?).

```python
"""PROJECTILE MOTION

Approximate simple projectile motion.
"""
__authors__ = ["Samuel J. Crawford", "Brooks MacLachlan", "W. Spencer Smith"]
__contact__ = "{craw.., machl.., smiths}@mcmaster.ca"
__date__ = "January 1st, 2019"
__license__ = "GPLv3-or-later"

# Imports
import math

# Constants
g = 9.8  # Gravity constant, m/s^2 (float)

# Inputs
s = 17.0  # Launch velocity, m/s (float)
Θ = math.pi / 4  # Launch angle, rad (float)

# Verify inputs
if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

# Calculations
t = 2 * s * math.sin(Θ) / g  # Flight time, s (float)
pl = s * t * math.cos(Θ)  # Landing position, m (float)
```

## Paperclip: More prominent comment-based headers for grouped code

```python
"""PROJECTILE MOTION

Approximate simple projectile motion.
"""
__authors__ = ["Samuel J. Crawford", "Brooks MacLachlan", "W. Spencer Smith"]
__contact__ = "{craw.., machl.., smiths}@mcmaster.ca"
__date__ = "January 1st, 2019"
__license__ = "GPLv3-or-later"

#-------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------

import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8  # Gravity constant, m/s^2 (float)

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

s = 17.0  # Launch velocity, m/s (float)
Θ = math.pi / 4  # Launch angle, rad (float)

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------
t = 2 * s * math.sin(Θ) / g  # Flight time, s (float)
pl = s * t * math.cos(Θ)  # Landing position, m (float)
```

## Nexus: More comments about variables and calculations (almost spamming)

```python
"""PROJECTILE MOTION

Approximate simple projectile motion.
"""
__authors__ = ["Samuel J. Crawford", "Brooks MacLachlan", "W. Spencer Smith"]
__contact__ = "{craw.., machl.., smiths}@mcmaster.ca"
__date__ = "January 1st, 2019"
__license__ = "GPLv3-or-later"

#-------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------

import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8  # Gravity constant (Gravity of Earth), m/s^2 (float)

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

s = 17.0  # Launch velocity (initial velocity of the projectile), m/s (float)
Θ = math.pi / 4  # Launch angle (angle at which projectile launched from ground), rad (float)

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

if s <= 0.0: raise ValueError("Velocity must be greater 0.0.")
if 0.0 >= Θ or Θ >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------
t = 2 * s * math.sin(Θ) / g  # Flight time (total time projectile in flight), s (float)
pl = s * t * math.cos(Θ)  # Landing position (total distance projectile travelled from launcher), m (float)
```

## Brimstone: Clearer variable names

```python
"""PROJECTILE MOTION

Approximate simple projectile motion.
"""
__authors__ = ["Samuel J. Crawford", "Brooks MacLachlan", "W. Spencer Smith"]
__contact__ = "{craw.., machl.., smiths}@mcmaster.ca"
__date__ = "January 1st, 2019"
__license__ = "GPLv3-or-later"

#-------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------

import math

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------

g = 9.8  # Gravity constant, m/s^2 (float)

#-------------------------------------------------------------------------------
# INPUTS
#-------------------------------------------------------------------------------

v_launch = 17.0  # Launch velocity, m/s (float)
angle_launch = math.pi / 4  # Launch angle, rad (float)

#-------------------------------------------------------------------------------
# VERIFY INPUTS
#-------------------------------------------------------------------------------

if v_launch <= 0.0: raise ValueError("Velocity must be greater 0.0.")
if 0.0 >= angle_launch or angle_launch >= math.pi / 2.0: raise ValueError("Launch angle must be within (0, pi/2)")

#-------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------
t = 2 * v_launch * math.sin(angle_launch) / g  # Flight time, s (float)
landing_position = v_launch * t * math.cos(angle_launch)  # Landing position, m (float)
```
