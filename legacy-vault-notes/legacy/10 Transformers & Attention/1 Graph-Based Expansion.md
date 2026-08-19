# 1. Graph-Based Expansion

Retrieve an initial entity/chunk, then expand to connected nodes.  
**Example:**
User asks:  
“What papers influenced Geoffrey Hinton’s work on transformers?”  
Pipeline:  
1. Retrieve node: Geoffrey Hinton  
2. Traverse graph to related papers / collaborators / citations  
3. Retrieve supporting documents for those nodes  
**Benefit:** Better multi-hop retrieval.  
  
  
  
  
  
**Multi-Hop Reasoning — The Key Advantage**  
Vector DBs retrieve isolated chunks. Knowledge graphs can **chain relationships** across many steps:  
  
Query: "What companies were founded by people who worked at PayPal?"  
  
Multi-hop traversal:  
  PayPal → [employed] → Peter Thiel → [founded] → Palantir  
  PayPal → [employed] → Elon Musk   → [founded] → Tesla, SpaceX  
  PayPal → [employed] → Reid Hoffman → [founded] → LinkedIn  
  
A vector DB would need to get lucky finding all these in one chunk.  
A knowledge graph answers this in one traversal.
