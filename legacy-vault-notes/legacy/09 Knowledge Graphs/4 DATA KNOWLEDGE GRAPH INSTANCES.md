# 4. DATA (KNOWLEDGE GRAPH INSTANCES)

#####################################################  
  
ex:Fido a ex:Dog ;  
    ex:hasOwner ex:Alice .  
  
ex:Alice a ex:Person .  
  
  
  
  

| Si quieres...                             | Mejor recurso         |
| ----------------------------------------- | --------------------- |
| Base general para grounding de entidades  | Wikidata              |
| Taxonomías limpias / jerarquías           | YAGO / WordNet        |
| Relaciones semánticas de lenguaje natural | ConceptNet / BabelNet |
| Geografía / lugares                       | GeoNames              |
| Reusar ontologías existentes              | LOV                   |
| Ontología formal de alto nivel            | OpenCyc / SUMO        |
| Biomedical / ecological vocabularies      | OBO / BioPortal       |
  
  
![Chunking](assets/1EA38E68-66E7-467C-9A2F-92CB3F798264.png)  
**Lo que cambia vs RAG clásico son dos cosas:**  
En la **indexación** agregas una segunda rama — además de chunking y embedding, extraes entidades y relaciones de los documentos con NER (Named Entity Recognition), y las guardas en un grafo tipo Neo4j con un schema definido por una ontología. Por ejemplo: (Apple) -[:VENDE]-> (iPhone) -[:DISPONIBLE_EN]-> (Europa).  
En la **consulta** el flujo se bifurca — la pregunta se analiza para detectar entidades, luego lanzas dos búsquedas en paralelo: una Cypher query en el KG que sigue relaciones entre entidades, y la búsqueda vectorial clásica. Fusionas ambos resultados y construyes un prompt que tiene tanto hechos estructurados del grafo como texto semántico de los chunks.  
  
RAG clásico busca por similitud semántica — encuentra texto parecido a la pregunta. KG-RAG además entiende relaciones entre entidades — puede responder "¿qué productos de Apple se venden en Europa?" siguiendo la cadena Apple → producto → región, algo que la búsqueda vectorial no puede hacer bien porque es una pregunta relacional, no semántica.  
**Cuándo usarlo:** cuando tu dominio tiene muchas relaciones entre entidades (productos, personas, organizaciones, normativas). No lo usas para documentación técnica simple — ahí el RAG clásico es suficiente y mucho más barato de mantener.  
  
  
**RDF + RDFS + SPARQL** es el stack semántico del W3C. Todo se representa como tripletas sujeto → predicado → objeto. RDFS define el schema formal (clases, subclases, propiedades), OWL añade lógica de inferencia, y SPARQL es el lenguaje de query. Se guarda en un **triplestore** como Apache Jena o GraphDB. Es un estándar abierto — cualquier sistema que hable RDF puede consumir tus datos. La desventaja es que es verboso y más lento para queries complejas.
