# RDF : Resource Description Framework

The Resource Description Framework (RDF) is a W3C standard framework for representing, exchanging, and connecting structured data on the Web. It models information as directed graphs, specifically through "[triples](https://www.google.com/search?q=triples&oq=resource+descr&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDMyMzdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&ved=2ahUKEwjjoaDW2oWUAxUvhf0HHcHoCIUQgK4QegYIAQgAEAQ)" (subject-predicate-object URI  :  Uniform resource identifier) using  [Internationalized Resource Identifiers](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier) (IRIs) to identify resources and relationships.   
  
![Resource Description Framework](assets/C71CDC47-FE79-40FC-AA71-30498159A4E0.png)  
  
URIs Identify and reference resources uniquely   
Literals Describe data values that don’t have separate existence   
  
Blank Nodes  
denote the existence of an individual with specific attributes, but without  
providing an identification or reference.  
  
Definitions:  
○ Let I denote the set of IRIs, L the set of RDF Literals and B the set of RDF  
blank nodes. The set of RDF terms is defined as I∪L∪B.  
  
○ An RDF triple t:=(s,p,o) is any element of the set (I∪B)⨉(I)⨉(I∪B∪L),  
where s∈(I∪B) is called the subject,  
p∈I is called the predicate and  
o∈(I∪B∪L) is called the object.  
○ An RDF graph G is a subset of (I∪B)⨉(I)⨉(I∪B∪L),  
i.e. an RDF graph is a set of RDF triples.  
  
Turtle serialisation : [https://zenodo.org/records/10043736](https://zenodo.org/records/10043736)  
  
  
Definitions:  
○ A term t is a word, compound word, or multi-word expression that in specific contexts is given specific meanings.  
### ○ A terminology or vocabulary V={t1,...,tn} is a set of terms used to describe data in a particular domain or set of domains.  
○ A schema is a formal description of the high-level structure of a dataset that may be used for a variety of purposes, including managing, storing, indexing, querying, validating, and/or reasoning over a dataset.  
○ A semantic schema is a schema that allows for defining the meaning of  
high-level terms (aka vocabulary or terminology)
