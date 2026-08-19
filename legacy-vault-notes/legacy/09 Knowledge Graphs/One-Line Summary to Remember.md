# One-Line Summary to Remember

**RDF** stores facts,
**Turtle** writes them,
**RDFS** adds simple schema,
**OWL** adds richer logic,
**SPARQL** queries everything.  
  
RDF Schema (Resource Description Framework Schema, variously abbreviated as RDFS, RDF(S), RDF-S, or RDF/S) is a set of classes with certain properties using the RDF extensible knowledge representation data model, providing basic elements for the description of ontologies.  
  
  
  
**Core Idea**  
A Knowledge Graph represents information as **entities (nodes)** and **relationships (edges)** between them. Instead of storing text and retrieving by similarity, you store *facts* and traverse *explicit connections*.  
  
Vector DB asks:   "what text chunks are similar to this query?"  
Knowledge Graph:  "what is the relationship between these specific entities?"  
  
  
(Paris) --[capital_of]--> (France)  
(France) --[located_in]--> (Europe)  
(Eiffel Tower) --[located_in]--> (Paris)  
(Eiffel Tower) --[built_by]--> (Gustave Eiffel)  
(Gustave Eiffel) --[born_in]--> (Dijon)  
**ELI5:** A vector DB is a library where you find books by how similar their covers look. A knowledge graph is a librarian who knows every book, every author, every relationship — and can answer *"find me all books by authors born in France who influenced Picasso"* in one traversal.  
  
**Quick Cheat Sheet**  

| Concept         | One-liner                                              |
| --------------- | ------------------------------------------------------ |
| Triple          | Subject → Predicate → Object, atomic unit of a KG      |
| Ontology        | Schema defining allowed entity types and relations     |
| Multi-hop       | Chain multiple relationships to answer complex queries |
| GraphRAG        | Build KG from docs, use graph + vector search together |
| TransE          | Learn entity/relation embeddings: h + r ≈ t            |
| Neo4j           | Most popular graph DB, Cypher query language           |
| Link prediction | Predict missing edges in the graph using embeddings    |
  
  
**Interview tip:** *"Vector DBs retrieve by proximity — they're great for unstructured text but can't reason about explicit relationships. Knowledge graphs store facts as triples and support multi-hop traversal — answering questions that require chaining several relationships. GraphRAG combines both: use vector search to find the entry point in the graph, then traverse to collect structured context. This is the current best practice for complex enterprise RAG applications where hallucination is costly."*  
  
GraphRAG  
*[https://arxiv.org/pdf/2404.16130](https://arxiv.org/pdf/2404.16130)*
