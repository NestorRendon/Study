# 4. OWL (Richer Ontology Logic)

Add stronger semantic knowledge:  
```

ex:Professor owl:equivalentClass ex:FacultyMember .


```
Meaning:  
Professor and FacultyMember are logically the same class.  
So if Alice is a Professor, infer:  
```

ex:Alice rdf:type ex:FacultyMember .


```
