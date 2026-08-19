# Induction, Deduction, Abduction

The terms infer/inference are often used almost interchangeably with  
entail/entailment.  
○ “entail” refers conceptually to what follows as a consequence,  
○ “infer” refers to a process of computing entailments and is very similar  
to “reason/reasoning”.  
● Deductive reasoning involves applying rules over premises to derive conclusions  
and is the main subject of Logic.  
● Inductive reasoning involves learning patterns from lots of examples and is the  
main subject of Machine Learning.  
● Abductive reasoning involves deriving a likely explanation for an observation  
  
**Abduction?**  
Abduction means:  
Inferring the best explanation for an observation.  
Example:  
  
Observation: Ground is wet  
Possible explanation: It rained  
And  
  
  
Yes — **OWL is designed to support deductive inference**.  
More precisely:  
OWL provides the logical semantics/axioms that allow a reasoner to perform deduction.  
  
**OWL → Deductive Inference**  
Example:  
If OWL says:  
  
ex:Professor rdfs:subClassOf ex:Person .  
  
And data says:  
  
ex:Alice rdf:type ex:Professor .  
  
A reasoner deduces:  
  
ex:Alice rdf:type ex:Person .  
  
That is standard OWL reasoning.  
  
  
In contrast to other data definition languages, RDF(S) is based on  
formal semantics.  
● Formal semantics enables RDF(S) to draw valid and sound logical  
inferences.
