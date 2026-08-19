# Attention is you need

https://jalammar.github.io/illustrated-transformer/  
  
![ENCODER](assets/FF89DF47-EEB4-453D-A985-F3DADC02216F.png)  
  
![feed Forward](assets/AA4D6DF3-5615-4525-9E36-0A032655C61C.png)  
self-attention layer – a layer that helps the encoder look at other words in the input sentence as it encodes a specific word. We’ll look closer at self-attention later in the post.  
  
  
![étudiant](assets/3D26EE81-A161-4AEA-9CE5-48B6A7884338.png)  
  
  
  
[https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello_t2t.ipynb](https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello_t2t.ipynb)  
  
  
The **first step** in calculating self-attention is to create three vectors from each of the encoder’s input vectors (in this case, the embedding of each word). So for each word, we create a Query vector, a Key vector, and a Value vector. These vectors are created by multiplying the embedding by three matrices that we trained during the training process.  
  
  
![Embedding](assets/F4069321-F883-4073-AC4E-57CA33AC9DAE.png)  
  
  
What are the “query”, “key”, and “value” vectors?

They’re abstractions that are useful for calculating and thinking about attention. Once you proceed with reading how attention is calculated below, you’ll know pretty much all you need to know about the role each of these vectors plays.  
The **second step** in calculating self-attention is to calculate a score. Say we’re calculating the self-attention for the first word in this example, “Thinking”. We need to score each word of the input sentence against this word. The score determines how much focus to place on other parts of the input sentence as we encode a word at a certain position.  
The score is calculated by taking the dot product of the query vector with the key vector of the respective word we’re scoring. So if we’re processing the self-attention for the word in position #1, the first score would be the dot product of q1 and k1. The second score would be the dot product of q1 and k2.  
  
  
  
![Embedding](assets/D2AB7E87-7DD6-4D04-A0BA-B96C1DAB6651.png)  
  
  
The **third and fourth steps** are to divide the scores by 8 (the square root of the dimension of the key vectors used in the paper – 64. This leads to having more stable gradients. There could be other possible values here, but this is the default), then pass the result through a softmax operation. Softmax normalizes the scores so they’re all positive and add up to 1.  
  
![Embedding](assets/0626C134-3E47-48A0-B208-B73415B21DFB.png)  
This softmax score determines how much each word will be expressed at this position. Clearly the word at this position will have the highest softmax score, but sometimes it’s useful to attend to another word that is relevant to the current word.  
  
The **fifth step** is to multiply each value vector by the softmax score (in preparation to sum them up). The intuition here is to keep intact the values of the word(s) we want to focus on, and drown-out irrelevant words (by multiplying them by tiny numbers like 0.001, for example).  
The **sixth step** is to sum up the weighted value vectors. This produces the output of the self-attention layer at this position (for the first word).  
  
![Embedding](assets/9522B548-48E2-48FA-AB40-FF58C0BFB5EF.png)  
That concludes the self-attention calculation. The resulting vector is one we can send along to the feed-forward neural network. In the actual implementation, however, this calculation is done in matrix form for faster processing. So let’s look at that now that we’ve seen the intuition of the calculation on the word level  
  
**Matrix Calculation of Self-Attention**  
**The first step** is to calculate the Query, Key, and Value matrices. We do that by packing our embeddings into a matrix X, and multiplying it by the weight matrices we’ve trained (WQ, WK, WV).  
![self-attention-matrix-calculation.png](assets/DCBD8174-C5BD-4936-87AC-F32FAA491676.png)  
Every row in the X matrix corresponds to a word in the input sentence. We again see the difference in size of the embedding vector (512, or 4 boxes in the figure), and the q/k/v vectors (64, or 3 boxes in the figure)  
  
**Finally**, since we’re dealing with matrices, we can condense steps two through six in one formula to calculate the outputs of the self-attention layer.  
![softmax](assets/314D3C86-33F2-4A94-9A49-8BAC9ACE4324.png)  
The self-attention calculation in matrix form
