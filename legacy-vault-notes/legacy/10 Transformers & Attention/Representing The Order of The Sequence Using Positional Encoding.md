# Representing The Order of The Sequence Using Positional Encoding

One thing that’s missing from the model as we have described it so far is a way to account for the order of the words in the input sequence.  
To address this, the transformer adds a vector to each input embedding. These vectors follow a specific pattern that the model learns, which helps it determine the position of each word, or the distance between different words in the sequence. The intuition here is that adding these values to the embeddings provides meaningful distances between the embedding vectors once they’re projected into Q/K/V vectors and during dot-product attention.  
  
![MEDDING](assets/A1F262B0-7392-4967-AA7E-694C76BAF805.png)  
To give the model a sense of the order of the words, we add positional encoding vectors -- the values of which follow a specific pattern.  
  
If we assumed the embedding has a dimensionality of 4, the actual positional encodings would look like this:  
![POSITIONAL](assets/3014581E-718B-40C4-8C7A-0B1DE302B7A8.png)  
A real example of positional encoding with a toy embedding size of 4  
**The Residuals**  
One detail in the architecture of the encoder that we need to mention before moving on, is that each sub-layer (self-attention, ffnn) in each encoder has a residual connection around it, and is followed by a [layer-normalization](https://arxiv.org/abs/1607.06450) step.  
![ENCODER #1](assets/CD005E52-F46D-4ED7-96D6-0393D8BBB45E.png)  
If we’re to visualize the vectors and the layer-norm operation associated with self attention, it would look like this:  
![Add & Normalize](assets/EA1CEFF6-6E47-4EA9-9684-7F7588F6A51B.png)  
This goes for the sub-layers of the decoder as well. If we’re to think of a Transformer of 2 stacked encoders and decoders, it would look something like this:  
![Asd & Normalize](assets/71E37703-8C41-478D-8EDC-3E21084F32D9.png)  
  
  
  
**The Decoder Side**  
Now that we’ve covered most of the concepts on the encoder side, we basically know how the components of decoders work as well. But let’s take a look at how they work together.  
The encoder start by processing the input sequence. The output of the top encoder is then transformed into a set of attention vectors K and V. These are to be used by each decoder in its “encoder-decoder attention” layer which helps the decoder focus on appropriate places in the input sequence:  
![Decoding timestep 2 3 4 5 6](assets/08E367A3-708D-4070-9E91-E270E1B55B99.gif)  
After finishing the encoding phase, we begin the decoding phase. Each step in the decoding phase outputs an element from the output sequence (the English translation sentence in this case).  
The following steps repeat the process until a special symbol is reached indicating the transformer decoder has completed its output. The output of each step is fed to the bottom decoder in the next time step, and the decoders bubble up their decoding results just like the encoders did. And just like we did with the encoder inputs, we embed and add positional encoding to those decoder inputs to indicate the position of each word.  
![Decoding time sten 1(2)3 4 5 6|](assets/6C7CFD31-B7A0-455D-8078-F4D6DF6034E1.gif)  
The self attention layers in the decoder operate in a slightly different way than the one in the encoder:  
In the decoder, the self-attention layer is only allowed to attend to earlier positions in the output sequence. This is done by masking future positions (setting them to -inf) before the softmax step in the self-attention calculation.  
The “Encoder-Decoder Attention” layer works just like multiheaded self-attention, except it creates its Queries matrix from the layer below it, and takes the Keys and Values matrix from the output of the encoder stack.  
  
**The Final Linear and Softmax Layer**  
The decoder stack outputs a vector of floats. How do we turn that into a word? That’s the job of the final Linear layer which is followed by a Softmax Layer.  
The Linear layer is a simple fully connected neural network that projects the vector produced by the stack of decoders, into a much, much larger vector called a logits vector.  
Let’s assume that our model knows 10,000 unique English words (our model’s “output vocabulary”) that it’s learned from its training dataset. This would make the logits vector 10,000 cells wide – each cell corresponding to the score of a unique word. That is how we interpret the output of the model followed by the Linear layer.  
The softmax layer then turns those scores into probabilities (all positive, all add up to 1.0). The cell with the highest probability is chosen, and the word associated with it is produced as the output for this time step
