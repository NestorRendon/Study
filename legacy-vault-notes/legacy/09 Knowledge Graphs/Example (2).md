# Example

```

ex:teaches rdfs:range ex:Course


```
  
**RDFLib - RDF Serialisation and Visualisation**  
  
[https://colab.research.google.com/drive/1qn41H0huz0R1mmUFKD4NOAUW0X9HHxX7](https://colab.research.google.com/drive/1qn41H0huz0R1mmUFKD4NOAUW0X9HHxX7)  
  
**RDF Graph Manipulation**  
  
[https://colab.research.google.com/drive/1ppbr3yE_cOPuqc_Ubjap3mt5xHvbnSO](https://colab.research.google.com/drive/1ppbr3yE_cOPuqc_Ubjap3mt5xHvbnSO)  
  
Complex query   
  
[https://query.wikidata.org/](https://query.wikidata.org/)  
  
PREFIX wd: <http://www.wikidata.org/entity/>  
PREFIX wdt: <http://www.wikidata.org/prop/direct/>  
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
SELECT ?authorLabel ?bookLabel ?date  
WHERE {  
?book wdt:P31 wd:Q47461344 .  
?book wdt:P50 ?author .  
?book wdt:P577 ?date .  
?book rdfs:label ?bookLabel  
FILTER (LANG(?bookLabel)="en")  
FILTER REGEX (?bookLabel,"mars$","i") .  
?author rdfs:label ?authorLabel  
FILTER (LANG(?authorLabel)="en") .  
} ORDER BY ?date   
  
Knowledge Representation Stack:  
  
OWL / RDFS   ← semantics / ontology layer  
RDF          ← graph data model  
Turtle       ← serialization syntax  
SPARQL       ← query language
