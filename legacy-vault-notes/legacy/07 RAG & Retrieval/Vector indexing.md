# Vector indexing

To accelerate similarity search in high-dimensional space, vector databases create indexes on stored vector embeddings. Indexing maps the vectors to new data structures, enabling faster similarity or distance searches between vectors.  
![Vector Embeddings](assets/A3F083D5-6BD3-4394-86BB-4F17792E3EBF.png)  
**Inverted File (IVF)**  
This is the most basic indexing technique. It splits the whole data into several clusters using techniques like K-means clustering. Each vector of the database is assigned to a specific cluster.   
  
  
**Navigable Small World (NSW)**  
Navigable Small World (NSW) is similar to a proximate graph where nodes are linked together based on how similar they are to each other. The greedy method is used to search for the nearest neighbor point.  
  
**How HNSW (**Hierarchical navigable small world**) is Developed**  
So, what happens in HNSW is that we take the motivation from the skip list, and it creates layers like the skip list. But for the connection between the data points, it makes a graph-like connection between the nodes. The nodes at each layer are connected not only to the current layer nodes but also to the nodes of the lower layers. The nodes at the top are very few and intensity increases when we go down to the lower layers. The last layer contains all the data points of the database. This is what the HNSW architecture looks like.  
Press enter or click to view image in full size  
  
  
![layer 2](assets/8CE6DA43-175F-4450-9744-612F0D5C98FD.png)  
  
Vector search  
[Vector search](https://www.ibm.com/think/topics/vector-search) is the retrieval layer of a vector database used to discover and compare similar data points. Rather than matching exact keywords or values,   
* **[Cosine similarity](https://www.ibm.com/think/topics/cosine-similarity):** Measures the angular distance between vectors to determine how aligned they are in direction.  
* **[Jaccard similarity](https://www.ibm.com/think/topics/jaccard-similarity):** Compares the overlap between two sets relative to their total elements  
  
  
![Onen source](assets/B26A5592-CE82-42F5-B555-007E3F089F00.webp)  
  
  
  
  
![PDF, web, De](assets/004093B7-E86C-44F4-B045-8966AB8882A0.png)  
**Flujo 1 — indexación** (lo haces una vez, offline):  
"Tomas los documentos, los divides en chunks de ~512 tokens con overlap, cada chunk lo conviertes en un vector con un modelo de embeddings, y los guardas en una base de datos vectorial."  
  
**Flujo 2 — consulta** (en tiempo real, cada pregunta):  
"La pregunta entra, primero verificas el cache de Redis. Si ya existe esa pregunta, devuelves la respuesta al instante. Si no, embedes la pregunta con el mismo modelo, haces una búsqueda ANN en el vector DB para sacar los top-k chunks más similares, inyectas esos chunks en el prompt junto con la pregunta, y se lo mandas al LLM. La respuesta la devuelves al usuario y la guardas en cache para la próxima vez."  
  
Mejorar, Dataset de testing de preguntas, mirar como se hace la indexación, probar la similaridad de embedings
