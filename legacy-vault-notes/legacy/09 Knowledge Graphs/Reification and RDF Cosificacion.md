# Reification and RDF (Cosificacion)

Reification in RDF means:  
**Turning a statement/triple into a thing you can talk about.**  
  
  
**Reification Solves This**  
You convert the triple into an object/node representing **the statement itself**.  
Then you can attach metadata to that statement.  
  
**Example**  
Instead of only:  
  
ex:Alice ex:worksAt ex:OpenAI .  
  
Reify it:  
  
ex:stmt1 rdf:subject ex:Alice ;  
         rdf:predicate ex:worksAt ;  
         rdf:object ex:OpenAI ;  
         ex:source "LinkedIn" ;  
         ex:confidence 0.92 .  
  
Reification is representing a triple as an entity so metadata can be attached to that triple.  
  
Reification is the fallacy of treating an abstract concept, idea, or social relation as a concrete, physical thing.  
  
RDF also permits the interleaving of statements,  
i.e. to make statements about statements  
  
rdf:Statement  
defines an RDF statement consisting of subject, predicate, obje  
  
  
Example:   
  
“ChatGPT states that Sherlock Holmes is a role model for Mr. Spock”.  
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .  
@prefix : <http://example.org/KG2023#> .  
:statement1 a rdf:Statement ;  
rdf:subject :SherlockHolmes ;  
rdf:predicate :roleModel ;  
rdf:object :Spock .  
:statement1 :statedBy :ChatGPT .  
  
  
○ Modeling data provenance  
○ Formalizing statements about reliability and trust  
○ Define metadata about statements  
● But you should be careful…  
○ Relations and classes can be transformed into instances  
potentially resulting in type conflicts  
○ Risk to define infinite recursions and cycles
