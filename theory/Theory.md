Jason's Ramblings
--

Is a `ChunkDB` a theory presentation? Maybe we should flush out this discussion
we've had in passing previously...
* Recall (I'm pulling this from Dr. Farmer's STT book): $T=(L,\Gamma)$, $T$ is a
  theory, $L$ is a language, $\Gamma$ is our set of axioms about $L$, $L=(B,C)$,
  $B$ is a set of base types, $C$ is a set of constant symbols.
* There is a meta-language for $\Gamma$. In STT, that is Alonzo. I'm not sure
  what ours is, but let's say it's Alonzo for now.
* A theory definition module presents $T$s in a human-readable fashion, e.g.,
  theory of monoids (pg. 97, STT):
  
  <img width="300" alt="Screenshot 2025-03-21 at 12 33 33 PM" src="https://github.com/user-attachments/assets/32aaa2ce-20a7-4833-bc05-c21bab2d658c" />
  
  Here, $T=((\set{S},\set{\cdot_{S \to S \to S},
  e_S}),\set{\text{associativity},\text{left identity},\text{right identity}})$.
* The theory definition module assigns a name to a theory and names to each of
  the axioms.



