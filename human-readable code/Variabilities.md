# Variabilities

4 levels at which variations occur, in order:

1. **“Domain Knowledge → Software Requirements Specification” Choices**
2. **“Software Requirements Specification → ICO Program Requirements” Choices**
3. **“ICO Program Requirements → Code” Choices**
4. **“Code → Artifacts” Choices**

First, a few notes about them, and then, long explanations of each one (in the subsections):

* These levels remain blurry, but are taking shape.
* Each “level” corresponds to a concrete phase we go through in the SmithEtAl code generator.
* There are 5 real stages of data:
  * Domain knowledge
  * Software Requirements Specification
  * ICO Program Requirements
  * "Code" (abstract software artifacts capturing program *flow*)
  * Artifacts
* Each of the 5 stages may be considered standalone “knowledge.”
* Each level establishes a dependency in the SmithEtAl toolchain. However, any of the first $n$ steps can be dropped in favour of manually writing the SRS/ICO Prog. Req/Code/Artifacts.

## “Domain Knowledge → Software Requirements Specification” Choices

The first phase is about building an (abstract) SRS (not a concrete artifact). It is about the design choices related to the derivation/construction of an SRS. So, the only kinds of choices here are related to domain expertise (domain being the type of background knowledge the problem belongs to, e.g., physics, chemistry, etc.). The kinds of choices available are tied to the kind of problem being defined. For example, an ICO problem will have formula choices possible. I highly doubt the “choices” here will ever be enumerated (because the number of choices here are likely infinite). However, there are some kinds of choices that will almost certainly always be relevant, such as *assumptions* (which includes *definitions*).

<hr>
<b>CONTINUE EDITING HERE!</b>
<hr>

## “Software Requirements Specification → ICO Program Requirements” Choices

Imagine a function that distills an ICO SRS into only the most fundamental parts a computable ICO problem needs. Another way to think of this is about SystemKinds. This function would strip down a SmithEtAl SRS of an ICO problem into just a list of inputs, exports, constraints, and variables, a set of formulas, and importantly: a list of “holes” (i.e., variables with missing formulas). This level will also perform type translations. For example, a Real would be translated to single/double/quadruple precision floating point number, a rational would be translated to a pair of signed integers, etc. The “ICO Program” type I’m imagining contains only “I want to compute these things. These are the bare minimum things you need to know as a software developer. Don’t worry about what any of these numbers really mean.” At this stage, variable descriptions at the SmithEtAl SRS level are used to produce comments on variables (e.g., comment format: “<NAME> [(<UNIT>, [<‘MATH’ TYPE>])]”).

## “ICO Program Requirements → Code” Choices

This stage is about building programming-language-level requirements, architectural requirements, and corresponding artifact requirements. The kinds of options that would appear here are “Big Picture Software Characteristics.” The “Code” would be a very generic clone of whatever kind of output programming language we’re interested in producing. For example, with an imperative language output choice, it would contain the flow of statements for each module, where variables and type definitions should be placed, etc. One important choice that needs to be made here is where inputs and outputs are placed and captured. Are they bundled together in a record? Etc. This stage removes the connotation of an ICO program, distilling into a virtual, generic set of software artifacts.

## “Code → Artifacts” Choices

This stage makes the final line decisions. It makes the most concrete choices about the final software artifacts. In some sense, this is where the least interesting choices are, including those about comment style, PL choice and the PL-specific choices, indentation style, module import style/export style, etc. For the variables with holes, assisted manual code snippet creation is necessary, and they would go here. For example, code related to ODEs.

## Caveats and other Notes

Note: the knowledge in the SmithEtAl SRS might “leak” across these passes. For example, an FR that says that input values must be exported would affect (3). The requirements set at any step can constrain the choices in the later stages.



Partial Evaluation may happen at two stages: software requirements → ICO program requirements, and ICO program requirements → code. Both are sources of error. In particular, for floating-point accuracy, e.g., floating point multiplication and division operate differently in rounding, with division being less error-prone (?) but more expensive compared to multiplication. Source: https://stackoverflow.com/questions/4125033/floating-point-division-vs-floating-point-multiplication

This is highlighted through En Route and Glider.
