# 2.4 Named Entity Recognition (NER)

identify and classify specific entities from unstructured text. These entities can be names of people, organizations, locations, dates, and more.   
NER converts [raw data](https://kanerika.com/glossary/raw-data/) into structured information, making it easier for machines to process and understand.  
  
Recall from [1.4 Graphs and Triples](https://www.google.com/url?q=https%3A%2F%2Fdocs.google.com%2Fpresentation%2Fd%2F147-hjulZqnsuSfK-66NGq8GfTTNmeUNjew5XjQ8IrzI%2Fedit%3Fusp%3Dsharing) that graphs are constructed from *triples*. Each triple is composed of two vertices connected with a directed edge. The *vertices* are the entities, while the *edges* represent the relationships that exist between an entity pair.  
  
https://medium.com/@kanerika/named-entity-recognition-a-comprehensive-guide-to-nlps-key-technology-636a124eaa46  
  
  
Named Entity Recognition (NER) acts as a fundamental bridge between unstructured text and structured knowledge bases (KBs), enabling the automatic extraction, classification, and linking of entities. By identifying key information—such as persons, locations, and organizations—NER transforms raw data into actionable knowledge.   
  
Most research on NER/NEE systems has been structured as taking an unannotated block of text, such as [transducing](https://en.wikipedia.org/wiki/Transduction_(machine_learning)):  
Jim bought 300 shares of Acme Corp. in 2006.  
into an annotated block of text that highlights the names of entities:  
[Jim]Person bought 300 shares of [Acme Corp.]Organization in [2006]Time.
