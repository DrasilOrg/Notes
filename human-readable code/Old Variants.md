1. [Scrappy](#scrappy)
2. [Vicinity](#vicinity)
3. [Universe](#universe)
4. [Torch](#torch)
5. [Edge](#edge)
6. [Mad Hatter](#mad-hatter)
7. [Foray](#foray)
8. [Boxer](#boxer)
9. [Pinball](#pinball)
10. [Omega](#omega)
11. [Sunset](#sunset)
12. [Steamroller](#steamroller)
13. [Volcano](#volcano)
14. [Pinnacle](#pinnacle)
15. [Starlight](#starlight)
16. [Coffee](#coffee)
17. [Paperclip](#paperclip)
18. [Nexus](#nexus)
19. [Brimstone](#brimstone)


### Scrappy

Extension of [Backhander](#backhander).

> Friendlier assertion messages

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

### Vicinity

Extension of [Scrappy](#scrappy).

> Switch to hard sanity constraints (written in the negative)

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

### Universe

Extension of [Vicinity](#vicinity).

> No constant folding (`... / 4.9` ~~> `2 * ... / 9.8`)

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

### Torch

Extension of [Universe](#universe).

> "Prominent" (for lack of better words) constants to variables

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

### Edge

Extension of [Torch](#torch).

> Move constants to optional function inputs

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

### Mad Hatter

Extension of [Edge](#edge).

> Impose constraints on optional inputs

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

### Foray

Extension of [Mad Hatter](#mad-hatter).

> Add function description to docstring

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

### Boxer

Extension of [Foray](#foray).

> Clarify `pt`'s description

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

### Pinball

Extension of [Boxer](#boxer).

> Include unit information in docstring's Args/Returns sections

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

### Omega

Extension of [Pinball](#pinball).

> Include unit information in docstring's function description

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

### Sunset

Extension of [Omega](#omega).

> Include type information in docstring

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

### Steamroller

Extension of [Subset](#sunset).

> Add type hints on function inputs

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

### Volcano

Extension of [Steamroller](#steamroller).

> Add type hints on function outputs

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

### Pinnacle

Extension of [Volcano](#volcano).

> Move constants to global variables

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

### Starlight

Extension of [Pinnacle](#pinnacle).

> Introduce simple program metainformation at top of file

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

### Coffee

Extension of [Starlight](#starlight).

> Comment-based headers for grouped code

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

### Paperclip

Extension of [Coffee](#coffee).

> More prominent comment-based headers for grouped code

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

### Nexus

Extension of [Paperclip](#paperclip).

> More comments about variables and calculations (almost spamming)

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

### Brimstone

Extension of [Nexus](#nexus).

> Clearer variable names

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
