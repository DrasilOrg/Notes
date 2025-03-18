# `Chunk`

Boxes of knowledge.

## Who

We will give you three examples of chunks with varying degrees of information
density/usability:
* A [dense](#dense) one.
* A [light](#light) one.
* A [trivial](#trivial) one.

### Dense

The [following
code](https://github.com/JacquesCarette/Drasil/blob/cd996e49b222deaf25bac195b16d34fd611138b2/code/drasil-data/lib/Data/Drasil/Theories/Physics.hs#L96-L108)
builds a chunk (`torqueDD`) that declares one formula for calculating torque:
```haskell
torqueDD :: DataDefinition
torqueDD = ddENoRefs torque Nothing "torque" [torqueDesc] 

torque :: SimpleQDef
torque = mkQuantDef QP.torque torqueEqn

torqueEqn :: Expr
torqueEqn = sy QP.positionVec `cross` sy QP.force

torqueDesc :: Sentence
torqueDesc = foldlSent [S "The", phrase torque, 
  S "on a body measures the", S "tendency" `S.of_` S "a", phrase QP.force, 
  S "to rotate the body around an axis or pivot"]
```

From top to bottom, we are declaring the following bits of knowledge:
1. How torque (`torqueDD`) can be defined along with some discussion of what
   torque means.
2. That `torque` (a symbol) may be calculated using a formula (`torqueEqn`).
3. The torque formula (`torqueEqn`): $\overrightarrow{p} \times
   \overrightarrow{F}$.
4. A discussion of what torque means (`torqueDesc`).

Reminder: Only `torqueDD` is considered a chunk! All other components are merely
components of the `torqueDD` chunk.

We call this chunk “dense” because there's a lot of usable knowledge here. With
it, we can synthesize new kinds of knowledge, such as code. For example, from
the torque equation, we can generate the following Java code: `Vector3D torque =
position.cross(force);`. Alternatively, we can generate the following LaTeX:
`\overrightarrow{T} := \overrightarrow{p} \times \overrightarrow{F}`. We can
also transform the equation to, say, inline another formula for
$\overrightarrow{p}$. We can also assert complex restrictions, such as that the
two crossed vectors must be of the same dimension, contain real ($\mathbb{R}$)
elements truncated to 4 significant digits, or that their elements must use the
same units.

### Light

The [following
code](https://github.com/JacquesCarette/Drasil/blob/cd996e49b222deaf25bac195b16d34fd611138b2/code/drasil-data/lib/Data/Drasil/Citations.hs#L50-L59)
defines an informationally “light” chunk:
```haskell
smithLai2005 = cInProceedings [spencerSmith, lLai]
  "A new requirements template for scientific computing"
  ("Proceedings of the First International Workshop on " ++
  "Situational Requirements Engineering Processes - Methods, " ++
  "Techniques and Tools to Support Situation-Specific Requirements " ++
  "Engineering Processes, SREP'05") 2005
  [ editor [pjAgerfalk, nKraiem, jRalyte], address "Paris, France"
  , pages [107..121], 
  note "In conjunction with 13th IEEE International Requirements Engineering Conference,"] 
  "smithLai2005"
```

### Trivial

## What



## Where

## When

## Why

## How
