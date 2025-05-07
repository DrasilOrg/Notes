# `ChunkDB`

Drasil's core “database” we register all [`Chunk`s](./Chunk.md)s in.

## Who

The [following
code](https://github.com/JacquesCarette/Drasil/blob/d4d4b4718d1158294c0376fadf3014e24d921974/code/drasil-database/lib/Database/Drasil/ChunkDB.hs#L160-L180):
```haskell
-- | Our chunk databases. \Must contain all maps needed in an example.\
-- In turn, these maps must contain every chunk definition or concept 
-- used in its respective example, else an error is thrown.
data ChunkDB = CDB {
  -- CHUNKS
    symbolTable           :: SymbolMap
  , termTable             :: TermMap 
  , defTable              :: ConceptMap
  , _unitTable            :: UnitMap
  , _dataDefnTable        :: DatadefnMap
  , _insmodelTable        :: InsModelMap
  , _gendefTable          :: GendefMap
  , _theoryModelTable     :: TheoryModelMap
  , _conceptinsTable      :: ConceptInstanceMap
  -- NOT CHUNKS
  , _labelledcontentTable :: LabelledContentMap -- TODO: LabelledContent needs to be rebuilt. See JacquesCarette/Drasil#4023.
  , _refTable             :: ReferenceMap -- TODO: References need to be rebuilt. See JacquesCarette/Drasil#4022.
  , _traceTable           :: TraceMap
  , _refbyTable           :: RefbyMap
  }
makeLenses ''ChunkDB
```

## What

The `ChunkDB` is a database where we aggregate all our `Chunk` instances.

## Where

For any Drasil-based project, there should be only one `ChunkDB` that `Chunk`s
are fed into and the generators query.

## When

The `ChunkDB` should prominently appear in 2 areas of code:
1. _Your code (as a user **of** Drasil)_. Here, you will feed your `Chunk`
   instances into the `ChunkDB`.
2. _Drasil's generators_. Here, Drasil's generators will take your chunks and
   use them to generate other things. Along the way, your chunks will reference
   other chunks. The generators will query the `ChunkDB` to resolve those
   references and operate with them as necessary.

## Why

## How
