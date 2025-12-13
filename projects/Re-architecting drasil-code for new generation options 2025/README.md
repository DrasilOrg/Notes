# Re-architecting `drasil-code` for new generation options

## Objectives

1. Unblock writing of the [Generating Human-Readable Code](#) paper.
2. Enable generating new kinds of software generation options in `drasil-code`
   and related packages, enough such that we generate the majority of the [New
   Code Variants](./NEW-PROJECTILE-VARIANTS.md) of [Projectile](#).

## Status

In progress.

## Related Issues and Pull Requests

* De-coupling `drasil-code` from `drasil-lang` and `drasil-printers`
  * [drasil-lang: Switch RawContent's CodeBlock constructor from using CodeExpr to Expr.](https://github.com/JacquesCarette/Drasil/pull/4497)
  * [Remove drasil-code-related re-exports from drasil-lang](https://github.com/JacquesCarette/Drasil/pull/4503)
  * [System: Replace polymorphic variable with CI for "system name" and add "program name" String field based on system name.](https://github.com/JacquesCarette/Drasil/pull/4504)
  * [drasil-docLang: Remove drasil-code dependency.](https://github.com/JacquesCarette/Drasil/pull/4542)

## TODOs

1. Write meaningful descriptions of each variant.
2. We should also have a file called "Variabilities.md" that just documents
   variabilities, indexed by which variant is applied to, to obtain the other
   variant.
3. We might also want NecessaryInformation.md that documents what information we
   need to have present to be able to generate each variant as output.

## Questions

1. Can we encode $g$s of force in Drasil?
2. Is `d`/`pl` the horizontal distance travelled or the landing position?
   Equivalent but different.
3. 4 stages: How are they seen given that DK can be separated from display
   knowledge in the SRS?
