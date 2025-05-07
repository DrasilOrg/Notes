# Equilibrium

First, let "term" be defined as follows (from [dictionary.com](https://www.dictionary.com/browse/term)'s definition):
>  a word or group of words designating something, especially in a particular field, as atom in physics, quietism in theology, adze in carpentry, or district leader in politics.

"Equilibrium" is a term found in at least two different domains (Economics and Physics) that means different things.

## Domains

### Economics

Let $S(p)$ and $D(p)$ represent the supply and demand curves of a market's
good/service (e.g., potatoes, apples, furniture, etc.). "Equilibrium" refers to
a "state" (as in, "condition" or "form") the market is considered to be in iff
the good/service is sold at "equilibrium price" ($p_e$; i.e., a point at which
$S(p_e)=D(p_e)$). If a market does not operate at its equilibrium price, there
is either an excess supply (i.e., $p > p_e \land S(p) > D(p)$) or excess demand ("dual").

Notes:
* If a market operates at equilibrium price, $q_e$ (which can be defined by either formula: $q_e=S(p_e)=D(p_e)$) is called the equilibrium quantity supplied and demanded.
* _Linear Model_: Assuming that $S(p)$ and $D(p)$ are linear (and conventional assumption that $S(p)$ and $D(p)$ are monotonically increasing and decreasing respectively), there is a unique equilibrium price ($p_e$). For $S(p)=m_1p+b_1$ and $D(p)=m_2p+b_2$, $p_e=I~p~.~S(p)=D(p)$, $p_e=I~p~.~(m_1p+b_1=m_2p+b_2) = \frac{b_2-b_1}{m_1-m_2}$
* _Graphical Convention_: Despite $p$ being the independent variable, when plotted, $p$ is often show on the $y$-axis (which is normally associated with the dependant variable). $Q$ (quantity) is placed along the $x$-axis, representing the supply or demand at specific prices.

### Physics

Pulling from [sciencedirect](https://www.sciencedirect.com/topics/engineering/mechanical-equilibrium):
> A system in thermodynamic equilibrium must satisfy three requirements:
> 
> 1. mechanical equilibrium means there are no unbalanced forces acting on any part of the system or on the system as a whole.
> 2. thermal equilibrium means there are no temperature differences between parts of the system or between the system and its surroundings.
> 3. chemical equilibrium means there are no chemical reactions within the system.

Hence, in STEM, there is at least 4 notions of equilibrium! Bias: Locally, I've seen the prefixes dropped in physics and economics. I wonder if _retaining the prefix_ is actually important and "equilibrium" might be an overloaded short-form for contexts with a single notion of equilibrium. For this writing, we will restrict ourselves to _mechanical equilibrium_ (as seen in undergraduate first-year Physics class).

While the English definition of mechanical equilibrium appears fine to me (to me), there is often an alternative definition that discusses the implications of such balanced forces:
> a state in which an object or a system is not undergoing any change in its motion.

**Note**: I will discuss equilibrium in the context of a single object. For a system, the following definitions must hold for each object within the system.

English Definitions:
1. Static equilibrium: where the object/system is "at rest" (not moving) and does not rotate.
2. Dynamic equilibrium: where the object/system is exclusively moving with constant linear velocity and/or rotating with constant [spin] angular velocity.
3. Translational equilibrium: component of equilibrium that indicates object/system is either at rest or moving with constant linear velocity.
4. Rotational equilibrium: component of equilibrium that indicates object/system is either not rotating or rotating with constant [spin] angular velocity.

"Mathematical" Definitions (in reverse order):
1. _Rotational equilibrium_: For an object, if the net torque ($\tau_{net} := \sum \tau$) is equal to the zero vector ($\tau = 0$), it is said to be in rotational equilibrium.
2. _Translational equilibrium_: One definition, one common expansion:
   1. For an object, if the net forces acting on the object ($F_{net} := \sum F$) is equal to the zero vector ($F_{net} = 0$), it is said to be in translational equilibrium.
   2. For an object, if the net forces acting on the object in each axis ($F_{net,d}$, for axis $d$, $F_{net,d} := \sum F_d$) is equal to zero, it is said to be in translational equilibrium. For a 3D space, this translates commonly (assuming $x$, $y$, $z$ convention) to: $(F_{net,x} = 0) \land (F_{net,y} = 0) \land (F_{net,z} = 0)$, or, more compactly: $F_{net,x} = F_{net,y} = F_{net,z} = 0$.
3. _Dynamic equilibrium_: An object is in dynamic equilibrium if it is in either
   translational and/or rotational equilibrium and if it is moving and/or
   rotating, respectively, it must do so in constant linear and/or angular
   velocity.
4. _Static equilibrium_: An object is in static equilibrium if it is in translational and rotational equilibrium, and it is at rest (i.e., linear velocity is the zero vector) and not rotating (i.e., angular velocity is the zero vector).

**Notes:**
1. An [old-looking NASA page](https://www.grc.nasa.gov/www/k-12/airplane/angdva.html) and [Wikipedia](https://en.wikipedia.org/wiki/Angular_velocity) is where I got my information about angular velocity from. I say this specifically because I only recall orbital angular velocity problems from undergrad and high school.
2. I add quotations around "Mathematical" in `"Mathemetical" Definitions (in reverse order):` because they are not purely mathematics. Pure mathematical expressions are only interspersed. A completely axiomatic definition would beg a bit more (soon).

## Codifying

First, we will review a little bit of Drasil-specific terminology, and then we will codify "equilibrium" with pseudocode.

### Chunk-related Terminology

* `NP`: A noun phrase. Alias: 'term.'
* `Sentence`: An English sentence.
* `ShortName`: A short version of a name appropriate for labels in TeX/HTML.
* `UID`: A globally unique identifier, across types, domains, etc. For the purposes of this writing, a unique `String`.
* <details>
  <summary><code>IdeaDict</code>: A declaration of a noun phrase along with an optional abbreviation.</summary>

  ```haskell
  -- | 'IdeaDict' is the canonical dictionary associated to an 'Idea'.
  -- Contains a 'UID' and a term that could have an abbreviation ('Maybe' 'String').
  --
  -- Ex. The project name "Double Pendulum" may have the abbreviation "DblPend".
  data IdeaDict = IdeaDict {
    _uu :: UID,
    _np :: NP,
    mabbr :: Maybe String
  }
  ```

  </details>
* <details>
  <summary><code>QuantityDict</code>: A declaration of a "quantity" containing a specific <code>IdeaDict</code>/'term' it is prescribing some sort of mathematical meaning to, space (type) information, a symbol (dependant on the 'stage'/context [SRS/Code]), and optionally a UnitDefn..</summary>

  ```haskell
  -- | QuantityDict is a combination of an 'IdeaDict' with a quantity.
  -- Contains an 'IdeaDict', 'Space', a function from 
  -- 'Stage' -> 'Symbol', and 'Maybe' a 'UnitDefn'.
  --
  -- Ex. A pendulum arm does not necessarily have to be defined as a concept before
  -- we assign a space (Real numbers), a symbol (l), or units (cm, m, etc.).
  data QuantityDict = QD { _id' :: IdeaDict
                         , _typ' :: Space
                         , _symb' :: Stage -> Symbol
                         , _unit' :: Maybe UnitDefn
                         }
  ```

  </details>
* <details>
  <summary><code>ConceptChunk</code>: An extension of an <code>IdeaDict</code> that declares an English description of the term (that the `IdeaDict` defines) within relevant domains (captured by `UID`s, normally points to other `IdeaDict`s or other `ConceptChunk`s).</summary>

  ```haskell
  -- | The ConceptChunk datatype records a concept that contains an idea ('IdeaDict'),
  -- a definition ('Sentence'), and an associated domain of knowledge (['UID']).
  --
  -- Ex. The concept of "Accuracy" may be defined as the quality or state of being correct or precise.
  data ConceptChunk = ConDict { _idea :: IdeaDict -- ^ Contains the idea of the concept.
                              , _defn' :: Sentence -- ^ The definition of the concept.
                              , cdom' :: [UID] -- ^ Domain of the concept.
                              }
  ```

  </details>
* <details>
  <summary><code>ConceptInstance</code>: An extension of a <code>ConceptChunk</code> that includes a reference address (display knowledge; as a `String`) and a `ShortName` (a label appropriate for public display in TeX/HTML).</summary>

  ```haskell
  -- | Contains a 'ConceptChunk', reference address, and a 'ShortName'.
  -- It is a concept that can be referred to, or rather, a instance of where a concept is applied.
  -- Often used in Goal Statements, Assumptions, Requirements, etc.
  --
  -- Ex. Something like the assumption that gravity is 9.81 m/s. When we write our equations,
  -- we can then link this assumption so that we do not have to explicitly define
  -- that assumption when needed to verify our work.
  data ConceptInstance = ConInst { _cc :: ConceptChunk , ra :: String, shnm :: ShortName}
  ```

  </details>
* <details>
  <summary><code>DefinedQuantityDict</code> (DQD): Very similar to a <code>QuantityDict</code>. In fact, it's almost a duplicate! The only explicit major difference is that it extends a <code>ConceptChunk</code> rather than an <code>IdeaDict</code>. This means that the DQD also comes with a <em>description</em> of the term defined with this DQD.</summary>

  ```haskell
  -- | DefinedQuantityDict is the combination of a 'Concept' and a 'Quantity'.
  -- Contains a 'ConceptChunk', a 'Symbol' dependent on 'Stage', a 'Space', and maybe a 'UnitDefn'.
  -- Used when we want to assign a quantity to a concept. Includes the space, symbol, and units for that quantity.
  --
  -- Ex. A pendulum arm can be defined as a concept with a symbol (l), space (Real numbers), and units (cm, m, etc.).
  data DefinedQuantityDict = DQD { _con :: ConceptChunk
                                 , _symb :: Stage -> Symbol
                                 , _spa :: Space
                                 , _unit' :: Maybe UnitDefn
                                 }
  ```

  </details>
* <details>
  <summary><code>QDefinition</code>: An extension of a <code>DefinedQuantityDict</code> with a formula (normally encoded with either <code>Expr</code>, <code>ModelExpr</code>, or <code>Literal</code>). For "function quantities," the "input variables" are given as <code>UID</code>s (assumed to be to <code>QuantityDict</code>s).</summary>

  ```haskell
  data QDefinition e where
    QD :: DefinedQuantityDict -> [UID] -> e -> QDefinition e
  ```

  </details>
* <details>
  <summary><code>TheoryModel</code>: .</summary>

  ```haskell
  -- | A TheoryModel is a collection of:
  --
  --      * tUid - a UID,
  --      * con - a ConceptChunk,
  --      * vctx - definition context ('TheoryModel's),
  --      * spc - type definitions ('SpaceDefn's),
  --      * quan - quantities ('QuantityDict's),
  --      * ops - operations ('ConceptChunk's),
  --      * defq - definitions ('QDefinition's),
  --      * invs - invariants ('ModelExpr's),
  --      * dfun - defined functions ('QDefinition's),
  --      * ref - accompanying references ('DecRef's),
  --      * lb - a label ('SpaceDefn'),
  --      * ra - reference address ('SpaceDefn'),
  --      * notes - additional notes ('Sentence's).
  -- 
  -- Right now, neither the definition context (vctx) nor the
  -- spaces (spc) are ever defined.
  data TheoryModel = TM 
    { _mk    :: ModelKind ModelExpr
    , _vctx  :: [TheoryModel]
    , _spc   :: [SpaceDefn]
    , _quan  :: [QuantityDict]
    , _ops   :: [ConceptChunk]
    , _defq  :: [ModelQDef]
    , _invs  :: [ModelExpr]
    , _dfun  :: [ModelQDef]
    , _rf    :: [DecRef]
    ,  lb    :: ShortName
    ,  ra    :: String
    , _notes :: [Sentence]
    }
  ```

  </details>
<!-- * <details>
  <summary><code></code>: .</summary>

  ```haskell

  ```

  </details> -->

### Drasil-related Terminology

Let's assume the following definitions:
* **Idea**:
* **Concept**:

### Implementation

See the [equilibrium](https://github.com/JacquesCarette/Drasil/tree/equilibrium) branch of the Drasil repository.

