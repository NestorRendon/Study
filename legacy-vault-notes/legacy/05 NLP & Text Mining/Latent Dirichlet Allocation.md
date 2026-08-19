# Latent Dirichlet Allocation.

Latent Dirichlet Allocation (LDA) is used to classify text in a document to a certain topic. It creates a Dirichlet distribution based on topic per document and word per topic model.  
  
How does LDA Work?  
1) LDA assigns words at random to k topic for each document, where k is the number of pre-defined topics.  
2) LDA computes for each document 'd' and each word 'w' in the text.  
	a.* P(topic(t) | document(d))*: Proportion of words allocated to subject t in document d.  
	b. *P(word(w) | topic(t))*: Proportion of topic t assignment over all documents derived from w.  
3) Given all of the other words and their topic assignments, reassign topic t to word w with probability p.  
4) Iterate multiple times until the topic assignment remains the same.  
  
![Topics](assets/0C77E5B5-4F14-4AD4-A3C1-80C102E5FC93.jpg)
