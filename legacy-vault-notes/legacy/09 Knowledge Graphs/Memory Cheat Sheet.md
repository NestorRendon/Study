# Memory Cheat Sheet

| Layer | Example Functions / Constructs | Purpose |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| RDF | Alice teaches ML / Triples (subject, predicate, object) | Graph data model for representing knowledge as relationships |
| Turtle | ex:Alice ex:teaches ex:ML . / Prefixes, blank nodes, literals | Human-readable syntax to serialize RDF |
| RDFS | rdfs:domain, rdfs:range, rdfs:subClassOf, rdfs:subPropertyOf | Basic schema definition and lightweight inference |
| OWL | owl:EquivalentClass, owl:Restriction, owl:someValuesFrom, owl:inverseOf, owl:TransitiveProperty | Advanced ontology modeling and logical reasoning |
| SPARQL | SELECT, ASK, CONSTRUCT, FILTER, OPTIONAL, UNION, GROUP BY | Query and manipulate RDF graphs |
| SHACL | sh:NodeShape, sh:PropertyShape, sh:minCount, sh:maxCount, sh:datatype, sh:class, sh:pattern , sh:minCount 1 ; sh:maxCount 1 ; sh:path :taxonomyID | Validate RDF graphs against structural and semantic constraints |
