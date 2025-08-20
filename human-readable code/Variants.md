# Variants

Each variant ($V_x$) is numbered. $0$ is the “worst” working prototype with
$+\infty$ being the unequivocally “best” possible version, somehow usable in
any/all “enterprise” scenarios.

These variants are meant to satisfy the requirements mentioned in
<https://github.com/JacquesCarette/Drasil/compare/main...FitFor-codeChanges>.

## [$V_0$: Works on my Machine](./V0.py)

$V_0$ is a standalone `.py` file, intended to be the “no white-space, obscure
identifiers, non-idiomatic, no comment” version of Projectile. $V_0$ goes
slightly beyond that, with missing input constraints, missing unit information,
folded constants ($4.9$ instead of $2.0 / g$), and encodes the absolute minimum
amount of problem knowledge in the programs input/output messages for a user of
the program (already familiar with the problem) to use it. $V_0$ is intended to
be unreadable but usable code that is heavily reliant on tacit knowledge and
frustrating to maintain.

## [$V_1$: Straight Line: Simple, Straightforward](./V1.py)

$V_1$ is also a standalone `.py` file with:

1. *Code implicitly organized into blocks of code (separated by blank lines).*
   Since Projectile is a small, uncomplicated problem, intuiting that is
   strictly ordered about minimum necessary preceding steps is possible. For
   example, `math` is not needed until `math.pi` is first referenced, so it
   won't be imported until just before that step.
2. *More “domain knowledge” showing.* That is, through:
   1. Units mentioned in `input` statements and comments.
   2. Moving special numbers into variables.
   3. New outputs ($p_{land}$ and $d_{offset}$).
   4. Prettier, more descriptive input and output messages.
   5. Imposing sanity constraints on inputs.

However, $V_1$ still leaves too much domain knowledge implicit (Why these
formulas? How were they derived?), is unconventionally structured (assuming the
program were extended, the structure would quickly become a maintainability
throttle), and is still difficult to read.

## [$V_2$: Layered Phases: Solo/tightknit-group project](./V2.py)

$V_2$ refines $V_1$ with:

1. *Layered code organization.* Code re-arranged into distinct phases: defining
   constants, reading inputs, checking input constraints, performing
   calculations, and writing outputs. The phases are separated by large banners
   mentioning what the next phase of the program is.
2. *A descriptive header.* A header that mentions what the program is for, its
   name and who authored it.

$V_2$ is meant to be the variant of Projectile that focuses on the programmer's
experience, working on the assumption the program will remain mostly the same.
$V_2$ is more likely to be acceptable in solo projects or as part of tightknit
group work. However, rationale for the formulas used in the calculations remains
tacit. The main deviation in the formulas used in $V_0$, $V_1$ and $V_2$ is in
$p_{land}$ ($t_{flight}$'s formula is noted to be a sub-expression of
$p_{land}$'s and so the cached calculation of $t_{flight}$ is reused).

## [$V_3$: ?](./V3.py)

## [$V_4$: Simulated Trajectory, Over-designed](./V4.py)
