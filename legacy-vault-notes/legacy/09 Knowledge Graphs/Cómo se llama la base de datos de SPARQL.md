# ¿Cómo se llama la "base de datos" de SPARQL?

Se llama **Triple Store** (o *RDF Store*). Es el motor de almacenamiento nativo para RDF.  
  
  
Tu "base de datos" SPARQL = Triple Store  
                            └── almacena triples: (sujeto, predicado, objeto)  
                            └── ejemplos: GraphDB, Apache Jena Fuseki,   
                                         Stardog, Amazon Neptune, Virtuoso  
Los términos se relacionan así:  
  
  
Knowledge Graph  
    │  
    ├── es el CONCEPTO (la red de entidades y relaciones con semántica)  
    │  
    └── vive DENTRO de un Triple Store (RDF) o Graph DB (LPG)  
                                │  
                                └── se consulta con SPARQL (si es RDF)  
                                    o Cypher (si es Neo4j/LPG)  
**Knowledge Base** es el término más amplio — incluye las ontologías, reglas, vocabularios controlados, y los datos. El Knowledge Graph es la instancia concreta de datos. El Triple Store es donde físicamente se guarda.  
  
  
  
OWL (Web Ontology Language) es el lenguaje con el que le dices al knowledge graph qué *significa* cada cosa — no solo cómo se llama, sino qué implica. Es la diferencia entre guardar datos y guardar conocimiento.  
La idea central: en RDF puro dices hechos. En OWL, dices **reglas** — y el razonador *deduce* hechos nuevos automáticamente.
