# 3. RDFS (Basic Schema / Typing)

Add domain/range information:  
```

ex:teaches rdfs:domain ex:Professor ;
           rdfs:range ex:Course .


```
Meaning:  
* whoever teaches is a Professor  
* whatever is taught is a Course  
From this, a reasoner infers:  
```

ex:Alice rdf:type ex:Professor .
ex:MachineLearning rdf:type ex:Course .


```
