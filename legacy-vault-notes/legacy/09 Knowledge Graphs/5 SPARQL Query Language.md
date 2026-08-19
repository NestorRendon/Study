# 5. SPARQL (Query Language)

Query the graph:  
```

SELECT ?x
WHERE {
  ?x rdf:type ex:FacultyMember .
}


```
Result:  
```

Alice


```
  
  
Example   
  
@prefix ex:   <http://example.org/> .  
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .  
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .  
@prefix owl:  <http://www.w3.org/2002/07/owl#> .  
@prefix sh:   <http://www.w3.org/ns/shacl#> .  
  
#####################################################
