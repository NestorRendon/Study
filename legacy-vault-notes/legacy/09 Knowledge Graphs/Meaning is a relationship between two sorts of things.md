# Meaning is a relationship between two sorts of things:

○ Signs and  
	○ the kinds of things they intend, express, or signify.  
● Words (and nonverbal symbols) are necessarily meaningful!  
  
Meaning refers to the significance, purpose, intention, or definition behind words, actions, concepts, or signs  
  
Understanding (in general) is the ability to grasp the meaning of  
information.  
● Information is conveyed in a message using a specific language from  
a sender to a receiver.  
Correct interpretation  depends on   
  
Syntax,   
Semantics,   
Context,   
Pragmatics,   
Experience   
   

| Concept    | Focus              | Key Question              |
| ---------- | ------------------ | ------------------------- |
| Syntax     | Structure          | Is it well-formed?        |
| Semantics  | Meaning            | What does it mean?        |
| Context    | Situation          | When/where does it apply? |
| Pragmatics | Use                | How is it used?           |
| Experience | Learning over time | What have we learned?     |
  
Lexical meaning refers to the specific, dictionary-definition meaning of a word in isolation, independent of its grammatical function, context, or surrounding words  
  
  
For successful communication,  
	○ information has to be correctly transmitted (Syntax)  
	○ the meaning (Semantics) of the transmitted information must be  
interpreted correctly (= understanding).  
● Understanding depends on  
	○ the context of both sender and receiver and  
	○ the pragmatics of the sender.  
● (Personal) experience determines  
how sender and receiver interpret the semantics, context, and  
pragmatics of a message, and thus its intended meaning.  
  
  
![An Intuitive Way to Represent Knowledge](assets/DFECD46F-EC45-4655-A688-76C501EF6EB1.png)  
  
A knowledge graph is a structured, semantic network representing real-world entities (people, places, concepts) as nodes and their relationships as edges, allowing machines to understand, integrate, and infer data  
  
[https://spacy.io/](https://spacy.io/)  
  
Python library to Industrial strength NLP   
  
Token object   
  
Lemma, part of speech tag,   
  
dependency parsing  
  
tokenization, lemmatization, Part-of-speech (POS) tagging and dependency parsing.  
  
  
**NLP Processing Concepts – Meanings and Examples**  

| Concept | Meaning (Distinct Role) | Key Question | Example Input | Example Output |
| ------------------ | --------------------------------------------------- | ----------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------- |
| Tokenization | Splits raw text into basic units (tokens) | How is the text segmented? | "The birds were singing loudly" | ["The", "birds", "were", "singing", "loudly"] |
| Lemmatization | Converts words to their canonical (dictionary) form | What is the base form of each word? | "birds", "singing" | "bird", "sing" |
| POS Tagging | Assigns grammatical roles to each token | What is each word’s grammatical function? | ["The", "birds", "were", "singing", "loudly"] | The (Det), birds (Noun), were (Verb), singing (Verb), loudly (Adverb) |
| Dependency Parsing | Identifies syntactic relationships between words | How are words structurally related? | "The birds were singing loudly" | subject(singing, birds); advmod(singing, loudly) |
  
**Lemmatization** falls under the umbrella of **morphological analysis**, the study of words. It requires morphological rules and a lexicon to reduce a word to its base form. In this way, words that have different inflections can be treated as the same item. For example, the auxiliary verbs *is*, *are*, *was*, and *were* are grouped together under the lemma *be*.  
  
Part-of-Speech (POS) tagging in NLP is the process of labeling each word in a text with its grammatical role (e.g., noun, verb, adjective) based on its definition and context.  
  
Parsing : análisis sintáctico   
Parsing in Natural Language Processing (NLP), or syntactic analysis, breaks down sentences into component parts to analyze their grammatical structure, producing a parse tree for machine understanding  
  
* **Noun Phrase (Subject):** The man  
* **Verb Phrase (Predicate):** opened the door  
* **Parts of Speech:** The (article), man (noun), opened (verb), door (noun).  
They are two distinct procedures: POS Tagging: each token gets assigned a label which reflects its word class. Parsing: each sentence gets assigned a structure (often a tree) which reflects how its components are related to each other.  
  
**Lemmatization and stemming** reduce inflected forms to a base: "running" → "run", "geese" → "goose".  
  
[Stemming](https://www.google.com/search?q=Stemming&sca_esv=345c4b3485fa4e30&sxsrf=ANbL-n7ugZtbruYJIwlyXSw83x7LD5Dwuw%3A1776920781450&ei=zajpacGaG57Ji-gPl7OJ-Q0&biw=944&bih=828&oq=stemming+vs+lein+nlp&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHN0ZW1taW5nIHZzIGxlaW4gbmxwKgIIADIGEAAYBxgeMggQABgFGAcYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIFEAAY7wUyBRAAGO8FSOUiUMsSWLYbcAJ4AZABAJgB1QSgAZkKqgEJMC4zLjEuNS0xuAEDyAEA-AEBmAIGoALVBcICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIHEAAYgAQYDcICBhAAGA0YHpgDAIgGAZAGCpIHBTIuMy4xoAf8HrIHBTAuMy4xuAfRBcIHBTAuNC4yyAcMgAgA&sclient=gws-wiz-serp&mstk=AUtExfD1uExfBvXkfCC0G5XtVNOIg75o8Nb2IapPAdtpQ8Nsd78mQBJBEa7xgZkhbnEbYarGdPWzC82dhyhILVk3EsJ3NAH7pfeMMvfin5T8Fy-RpRjZOeJemvqWCGMXi_41GYK8VoseaBOnJrapu9xfQ2p08ALiLZ_hLwjwpuzXZEVhU_MqyQSNcnJJQnxNniJ0hjZZ&csui=3&ved=2ahUKEwjutZLmmYOUAxUp7wIHHbjxDrMQgK4QegQIARAD) and [lemmatization](https://www.google.com/search?q=lemmatization&sca_esv=345c4b3485fa4e30&sxsrf=ANbL-n7ugZtbruYJIwlyXSw83x7LD5Dwuw%3A1776920781450&ei=zajpacGaG57Ji-gPl7OJ-Q0&biw=944&bih=828&oq=stemming+vs+lein+nlp&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHN0ZW1taW5nIHZzIGxlaW4gbmxwKgIIADIGEAAYBxgeMggQABgFGAcYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIFEAAY7wUyBRAAGO8FSOUiUMsSWLYbcAJ4AZABAJgB1QSgAZkKqgEJMC4zLjEuNS0xuAEDyAEA-AEBmAIGoALVBcICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIHEAAYgAQYDcICBhAAGA0YHpgDAIgGAZAGCpIHBTIuMy4xoAf8HrIHBTAuMy4xuAfRBcIHBTAuNC4yyAcMgAgA&sclient=gws-wiz-serp&mstk=AUtExfD1uExfBvXkfCC0G5XtVNOIg75o8Nb2IapPAdtpQ8Nsd78mQBJBEa7xgZkhbnEbYarGdPWzC82dhyhILVk3EsJ3NAH7pfeMMvfin5T8Fy-RpRjZOeJemvqWCGMXi_41GYK8VoseaBOnJrapu9xfQ2p08ALiLZ_hLwjwpuzXZEVhU_MqyQSNcnJJQnxNniJ0hjZZ&csui=3&ved=2ahUKEwjutZLmmYOUAxUp7wIHHbjxDrMQgK4QegQIARAE) are text normalization techniques in NLP that reduce words to their base forms, though they differ in method and accuracy. Stemming is a fast, rule-based approach that crudely chops off word endings (e.g., "studies"   
  
 "studi"). Lemmatization is more accurate, using vocabulary and morphological analysis to return valid, dictionary-meaning words (e.g., "studies"  "study").   
  
  
**Stemming vs. Lemmatization Comparison**  
* **Methodology:** Stemming removes suffixes using crude rules; Lemmatization uses linguistic context and dictionaries.  
* **Output Quality:** Stemming often produces non-words ("chang" for "changing"); Lemmatization always produces valid dictionary words.  
* **Context Awareness:** Lemmatization understands that "better" becomes "good" (POS tagging); Stemming does not.  
* **Speed:** Stemming is generally faster and computationally cheaper; Lemmatization is slower.
