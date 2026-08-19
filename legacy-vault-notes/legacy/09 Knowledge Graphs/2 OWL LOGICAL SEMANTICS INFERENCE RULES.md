# 2. OWL (LOGICAL SEMANTICS / INFERENCE RULES)

#####################################################  
  
ex:PetDog a owl:Class ;  
    owl:equivalentClass [  
        a owl:Class ;  
        owl:intersectionOf (  
            ex:Dog  
            [ a owl:Restriction ;  
              owl:onProperty ex:hasOwner ;  
              owl:someValuesFrom ex:Person ]  
        )  
    ] .  
  
#####################################################
