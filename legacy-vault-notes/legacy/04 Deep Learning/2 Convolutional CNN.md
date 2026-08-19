# 2. Convolutional (CNN)

A small filter (kernel) slides over the input, detecting local patterns. Same filter reused everywhere — that's *weight sharing*.  
  
  
Filter 3×3 slides over image → detects edges, textures, shapes  
Early layers → edges  
Middle layers → shapes  
Deep layers → faces, objects  
**Use:** images, time series, any data with local structure. **Key params:** kernel size, stride, padding, number of filters.  
![The convolutional layer](assets/D610F9C4-F5D5-48AF-8ADE-7986B348CE3E.png)  
https://www.superannotate.com/blog/guide-to-convolutional-neural-networks
