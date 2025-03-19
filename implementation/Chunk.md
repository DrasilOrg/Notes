# `Chunk`

Statements of fact implemented with record `data` types (in Haskell).

## Who

We will give you three examples of chunks with varying degrees of information
density/usability:
* A [dense](#dense) one.
* A [light](#light) one.
* A [meaningless](#meaningless) one.

<div style="width: 100%; background-color: yellow; padding: 10px; color: black;">
    ⚠️ Note: the definition of the above three terms is imperfect.
</div>

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
We call this one “light” because there's little we can do with it apart from
simple rendering. Yes, we can calculate various statistics (e.g., how many times
we cite specific authors, years our cited works were most published, journals we
find ourselves citing the most, etc.), but from the perspective of a software
engineer, there's just not much we can do with this information other than
generate pretty, correctly formatted bibliographies. Additionally, there's
little we can do to audit any of the information in it. There's little internal
consistency we can enforce.

### Meaningless

By “meaningless,” we mean _to the computer_. These chunks are like prescriptions
of a new character you've never seen before. They mean nothing. It's only
through building relations between them and other things, that they may become
usable in some way. “There's almost no substance to these definitions.” For
example, the [following
code](https://github.com/JacquesCarette/Drasil/blob/d4d4b4718d1158294c0376fadf3014e24d921974/code/drasil-data/lib/Data/Drasil/Concepts/Math.hs#L25-L34)
defines a few mathematical concepts, but only in English statements (rewritten
for space):
```haskell
amplitude, angle, area, ... :: ConceptChunk
amplitude = dcc "amplitude"
    (nounPhraseSP "amplitude")
    "The peak deviation of a function from zero"
angle = dcc "angle"
    (cn' "angle")
    "the amount of rotation needed to bring one line or plane into coincidence with another"
area = dcc "area"
    (cn' "area")
    "a part of an object or surface"
```

These chunks, alone, are essentially meaningless. You can try using them to
generate anything non-trivial/naïve, and you'll quickly understand what we mean.
They are normally either ripe for reconstruction (with more meaningful records
that we can use for software generation), or, they're just very abstract and
only give us anything through surrounding chunks giving us tidbits of knowledge
about them. 

TODO: Example of both situations. I'm not confident that this is a good
definition. I think the former is okay, but I'm not sure if I can come up with a
good example of the latter. It's more like a constant symbol?

<!-- <div style="width: 100%; background-color: yellow; padding: 10px; color: black;">
    ⚠️ Note: 
</div> -->

## What

Chunks are _statements of fact_. With Haskell, we implement them as record
`data` types carrying a unique identifier (a `UID`) at minimum. Normally, we
want them to also declare noun (which can be compound/a noun phrase). For
example, “torque” alone might denote an abstract concept of torque and “torque
acting on the screw” might denote a specific instance of torque with a specific
mathematical symbol, defining expression, and so on.

## Where

TODO.

## When

Instances of `Chunk` are _only created by users of Drasil_. If Drasil were a
compiler, you may think of `Chunk`s as pieces of a library you would import.
Explicitly, `Chunk`s are only _referenced_ during the generation (compilation)
step, and no new `Chunk`s should be created through Drasil's generators.

## Why

TODO.

## How

The general form of a chunk definition is as follows:
```haskell
data Author = Author {
    uid :: UID,
    person :: Person,
    penName :: Text,
    ...
}
```

With Drasil, this looks more like:
```haskell
data Author = Author {
    _aUID :: UID,
    _aPerson :: Person,
    _aPenName :: Text,
    ...
}
makeLenses ''MyChunk

instance HasUID         MyChunk where uid = aUID
...
```
This is because of Drasil's code style guide preferring the use of classy
lenses.

<div style="width: 100%; background-color: yellow; padding: 10px; color: black;">
    ⚠️ Note: While the above code snippets show `Person` as part of `MyChunk`,
    if `Person` were a `Chunk` as well, then `Person` should really be 
    `Ref Person` (i.e., a reference to a person). Unfortunately, at the moment,
    this is not done as often as we would like it to be in Drasil.
</div>
