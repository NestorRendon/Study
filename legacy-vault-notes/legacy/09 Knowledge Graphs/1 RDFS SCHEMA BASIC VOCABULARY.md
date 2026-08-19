# 1. RDFS (SCHEMA / BASIC VOCABULARY)

#####################################################  
  
ex:Dog a rdfs:Class .  
ex:Person a rdfs:Class .  
  
ex:hasOwner a rdf:Property ;  
    rdfs:domain ex:Dog ;  
    rdfs:range ex:Person .  
  
#####################################################
