# Dataset Size Graph (Performance vs. Dataset Size)

* **Purpose:** The primary use of this graph (often called a **learning curve based on data size**) is to **evaluate the efficiency of the model architecture relative to the amount of training data** and determine how much data is necessary to reach optimal performance.  
* **X-axis:** The size (or number of unique data points) of the training dataset used. This measures unique data points seen once, regardless of how many epochs are run.  
* **Y-axis:** A performance metric, such as accuracy or error rate.  
* **Analysis:**  
    * Performance typically increases as the dataset size grows and eventually saturates.  
    * If the performance saturates, adding more data is unlikely to significantly improve the model further, suggesting the model has learned the general distribution of the data well.  
    * This graph helps compare the *data efficiency* of different algorithms by showing how much data each requires to reach a certain performance level
