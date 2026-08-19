# 3. SHACL (VALIDATION RULES / CONSTRAINTS)

#####################################################  
  
ex:DogShape a sh:NodeShape ;  
    sh:targetClass ex:Dog ;  
  
    sh:property [  
        sh:path ex:hasOwner ;  
        sh:minCount 1 ;  
        sh:maxCount 1 ;  
        sh:class ex:Person ;  
    ] .  
  
#####################################################
