# dependency parsing

is a process that determines and examines the grammatical relationships between phrases and words in a sentence.  
Each relationship is indicated by a **head** (tail of the arrow) and its modifiers, the **dependent**/s (tip of the arrow). In the diagram below, *born* is considered the head, *was* as the tail, and [auxpass](https://www.google.com/url?q=https%3A%2F%2Funiversaldependencies.org%2Fdocs%2Fen%2Fdep%2Fauxpass.html) for passive auxiliary  
  
![sexpass](assets/9F9FFD08-76F4-42FB-ADB7-E0CEA1C10324.png)  
  
Dependency parsing in NLP identifies grammatical relationships between words by connecting them to heads in a tree-like structure, defining roles like subject, object, or modifier.   
  
[https://www.geeksforgeeks.org/nlp/dependency-parsing-with-nltk/](https://www.geeksforgeeks.org/nlp/dependency-parsing-with-nltk/)  
![admod amod](assets/11A9317C-167F-4858-AA8C-47C637F45DE2.webp)  
> ***PP:**** Personal Pronoun (“I”)
**VBD: **Verb (“saw”)
**DT:** Determiner (“the”)
**INN: **Noun, direct object
**IN: **Preposition (“with”)
**RB: **Adverb (“very”)
**JJ:** Adjective (“Strong")
**NN: **Noun (“binocular”)*  
>   
These terms represent specific dependency labels used in natural language processing (NLP)   
* **nsubj (Nominal Subject):** A noun phrase that is the syntactic subject of a clause.  
    * *Example:* [**She**] runs. (nsubj(runs, She))  
* **compound:** A noun that modifies another noun, often part of a compound word.  
    * *Example:* [**Wall**] Street. (compound(Street, Wall))  
* **nsubjpass (Passive Nominal Subject):** A noun phrase that is the syntactic subject of a passive clause.  
  
[https://universaldependencies.org/docsv1/pl/dep/all.html](https://universaldependencies.org/docsv1/pl/dep/all.html)* *  
  
  
> ![Dependency Type](assets/0B976AB7-8BBB-4C7E-BF60-87921C9FA7B9.png)  
  
![D is likely a dependent of head H in construction C:](assets/DD182A72-29E2-41AD-B499-DF1F7292902B.png)
