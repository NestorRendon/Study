# The Beast With Many Heads

The paper further refined the self-attention layer by adding a mechanism called “multi-headed” attention. This improves the performance of the attention layer in two ways:  
1. It expands the model’s ability to focus on different positions. Yes, in the example above, z1 contains a little bit of every other encoding, but it could be dominated by the actual word itself. If we’re translating a sentence like “The animal didn’t cross the street because it was too tired”, it would be useful to know which word “it” refers to.  
2. It gives the attention layer multiple “representation subspaces”. As we’ll see next, with multi-headed attention we have not only one, but multiple sets of Query/Key/Value weight matrices (the Transformer uses eight attention heads, so we end up with eight sets for each encoder/decoder). Each of these sets is randomly initialized. Then, after training, each set is used to project the input embeddings (or vectors from lower encoders/decoders) into a different representation subspace.  
![Thittona l](assets/65E36ED1-553A-4862-863C-87E92875D4E1.png)  
With multi-headed attention, we maintain separate Q/K/V weight matrices for each head resulting in different Q/K/V matrices. As we did before, we multiply X by the WQ/WK/WV matrices to produce Q/K/V matrices.  

If we do the same self-attention calculation we outlined above, just eight different times with different weight matrices, we end up with eight different Z matrices  
![Machines HE](assets/CA101FA4-DB90-492E-AFA9-A31B4F570205.png)  
  
This leaves us with a bit of a challenge. The feed-forward layer is not expecting eight matrices – it’s expecting a single matrix (a vector for each word). So we need a way to condense these eight down into a single matrix.  
How do we do that? We concat the matrices then multiply them by an additional weights matrix WO.  
![1) Concatenate all the attention heads](assets/D16FBBA2-5355-482B-96A5-566283C7BC84.png)  
That’s pretty much all there is to multi-headed self-attention. It’s quite a handful of matrices, I realize. Let me try to put them all in one visual so we can look at them in one place  
  
![input sentence" each word](assets/E8A5CEC3-62B3-488A-AA4D-8685459C7EA6.png)  
  
Now that we have touched upon attention heads, let’s revisit our example from before to see where the different attention heads are focusing as we encode the word “it” in our example sentence:  
![Layer: 5 ÷ Attention: Input - Input](assets/4EDAD1FE-D670-488E-A2E5-344A7F9D21D1.png)  
As we encode the word "it", one attention head is focusing most on "the animal", while another is focusing on "tired" -- in a sense, the model's representation of the word "it" bakes in some of the representation of both "animal" and "tired".  
  
If we add all the attention heads to the picture, however, things can be harder to interpret:  
![Layer: 5 ÷ Attention: Input - Input](assets/6B8D6E5B-8971-4CF5-9078-0971C063D329.png)
