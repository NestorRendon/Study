# RDF Schema, officially called “RDF Vocabulary Description Language

RDF Classes and properties provide a high-level vocabulary –  
a set of RDF terms – for general use in RDF descriptions.  
● Vocabularies can be easily reused across different  
independent RDF sources.  
● Datasets that agree on vocabularies are better integrable  
since they “speak the same language”.  
● Naming convention:  
○ Classes are given upper case singular names  
(:Occupation, :Person, :FictionalCharacter, …)  
○ Properties are given lower case singular names  
  
  
RDF Schema allows:  
○ Definition of classes via rdfs:Class  
○ Class instantiation in RDF via rdf:type  
○ Example:  
:Person rdf:type rdfs:Class .  
:LeonardNimoy rdf:type :Person .  
  
RDFS Meta-Classes:  
Everything in the RDF model is a resource  
  
Definition of hierarchical relationships:  
○ Subclasses and superclasses via rdfs:subClassOf  
  
RDFS Annotation Properties  
to annotate resources with useful (human-readable) information.  
○ rdfs:seeAlso defines a relation of a resource to another, which explains it  
○ rdfs:isDefinedBy subproperty of rdfs:seeAlso, defines the relation of a resource to Its definition  
○ rdfs:comment comment, usually as text  
○ rdfs:label “readable” name of a resource (contrary to ID)
