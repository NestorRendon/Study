# Hypothesis testing (What is it, and why would you need it?)

Statistical hypothesis testing involves making a decision about two competing hypotheses. The null hypothesis (𝐻0  
) is a statement about the assumed value of a population parameter. It is usually a hypothesis about no difference or no relationship. The alternative hypothesis (𝐻1  
) is a statement about the value of a population parameter that you want to test. It is usually a hypothesis that has some difference or some relationship.  
  
1. Determine the null (𝐻0) and alternative (𝐻1) hypotheses. The null hypothesis is assumed to be true when you start your analysis. It is the logical opposite of your suspicion.  
2. Select a significance level. The significance level is the amount of evidence needed to overturn your assumption that the null hypothesis is true.  
3. Collect evidence (data).  
4. Use a decision rule to make a judgment. If the evidence in the data is sufficiently strong, based on the selected significance level, then reject the null hypothesis. If the evidence in the data is not strong enough, fail to reject the null hypothesis. It is important to note, however, that failing to reject the null hypothesis does not prove the alternative hypothesis.  
  
What is a *p*-value?  
A reference distribution enables you to quantify the probability of observing a particular outcome (the calculated test statistic) or a more extreme outcome if the null hypothesis is true. That probability is called the *p*-value.  
A large *p*-value indicates a high probability of observing your results or more extreme results, given that 𝐻0  
  
 is true. Therefore, it is reasonable to continue to assume 𝐻0  
 is true, and you fail to reject the null hypothesis. A small *p*-value indicates a low probability of observing your results or more extreme results, given that 𝐻0  
 is true. Therefore, it is no longer reasonable to assume that 𝐻0  
 is true, and you reject the null hypothesis.  
The *p*-value is a number between zero and one, inclusive. It is a probability that is calculated from your data.  
  
The null hypothesis  is often described as "negative" because it typically represents a position of **no effect**, **no difference**, or **no relationship** between variables. It acts as the default "status quo" or "nothing" hypothesis that researchers aim to test, or "disprove," through statistical evidence  
  
  
Name some different sampling procedures (e.g. random, stratified, Poisson disc, among others).  

| Sampling Procedure | Description | Advantages | Disadvantages | Typical Applications |
| ------------------------ | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Random Sampling | Each sample has an equal probability of being selected. | Simple to implement; statistically unbiased; easy to analyze; good baseline method. | Can produce clusters or gaps; poor spatial coverage; higher variance in heterogeneous environments. | General statistics, ML dataset splitting, baseline ecological studies. |
| Stratified Sampling | Population divided into strata (groups) and sampled within each stratum. | Ensures representation of different groups; reduces variance; good for heterogeneous populations. | Requires prior knowledge to define strata; incorrect stratification may introduce bias; more complex design. | Ecology, habitat studies, socioeconomic surveys, environmental monitoring. |
| Systematic Sampling | Samples collected at regular intervals (e.g., grid or every k units). | Good spatial coverage; easy to implement; efficient in field surveys. | Can introduce bias if periodic patterns exist in the data; randomness is limited. | Forestry surveys, agricultural monitoring, spatial sampling. |
| Cluster Sampling | Population divided into clusters and some clusters are sampled entirely. | Cost-efficient when populations are geographically dispersed; reduces travel/logistics costs. | Higher sampling error; clusters may not represent the whole population well. | Large-scale field surveys, household surveys, ecological monitoring. |
| Poisson Disc Sampling | Random sampling with a minimum distance constraint between samples. | Produces evenly distributed samples; avoids clustering; good spatial coverage; useful for spatial analysis. | More complex algorithm; computationally heavier; not purely random. | Computer graphics, spatial ecology, environmental monitoring. |
| Latin Hypercube Sampling | Multidimensional sampling ensuring coverage across each variable range. | Efficient exploration of parameter space; fewer samples needed than random sampling; good for simulations. | More complex to design; not ideal for spatial constraints alone. | Sensitivity analysis, simulation studies, environmental modeling. |
| Adaptive Sampling | Sampling intensity changes depending on observed values (e.g., more samples where phenomena occur). | Efficient for detecting rare or clustered events; focuses effort where needed. | Harder statistical inference; requires dynamic design during sampling. | Rare species surveys, ecological hotspot detection. |
  
  
  
Math  
- Matrix multiplication, identity, inversion, determinant, chain of products, systems of equations.  
  
![A =3](assets/15983645-FD6A-4718-8965-85EEF0DC60A9.png)  
![5. Matrix Inverse](assets/2D85D8E1-CD90-4B70-9B28-6780F8F994B8.png)  
  
  
  
![6. Determinant](assets/B943F77B-9B26-4887-B970-AAE2C5E09C2B.png)  
  
Producto punto   
  
![Ä•B= Ă B cos0](assets/CA8F34FE-FC06-41CD-950C-0EDD0B98E756.png)  
![A. B = AB cos(0)](assets/12231496-6026-469E-BC3D-75D190DC2D55.png)  
El producto punto es una manera fundamental en la que podemos combinar dos vectores. De manera intuitiva, nos dice algo acerca de qué tanto apuntan dos vectores en la misma dirección.  
  
**Matrix chain multiplication** (or the **matrix chain ordering problem**[[1]](https://en.wikipedia.org/wiki/Matrix_chain_multiplication#cite_note-Schwartz-1)) is an [optimization problem](https://en.wikipedia.org/wiki/Optimization_problem) concerning the most efficient way to [multiply](https://en.wikipedia.org/wiki/Matrix_multiplication) a given sequence of [matrices](https://en.wikipedia.org/wiki/Matrix_(mathematics)). The problem is not actually to *perform* the multiplications, but merely to decide the sequence of the matrix multiplications involved. The problem may be solved using [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming).  
![There are many options because matrix mutiplication is associative. In other words, no matter how the product is parenhesized, the](assets/56BDA068-EBC7-4FAF-ACF3-1617779168B8.png)  
  
-Derivatives, integrals, limits  
  
![1. Limits (Límites)](assets/7B7902E1-13D3-42F0-AD30-1552CF9E2C3C.png)  
  
**2. Derivatives (Derivadas)**  
**Meaning**  
A **derivative** measures **how fast something changes**.  
It represents the **rate of change** of a function.
