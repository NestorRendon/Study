# Key Differences Between ANOVA and ANCOVA

| Feature | ANOVA | ANCOVA |
| --------- | ------------------------------------- | -------------------------------------------- |
| Variables | Categorical IV, Continuous DV | Categorical IV, Continuous DV + Covariate(s) |
| Control | No control for external factors | Controls for covariates (e.g., baseline) |
| Goal | Simple group comparison | Comparison adjusted for external variance |
| Power | Lower if uncontrolled variables exist | Higher by reducing error term |
  
  
  
![Core set is nein pairs the random arables cand](assets/F91649D1-84DB-4D95-A6EC-0E8A0D1B3D49.png)  
  
Bayesian Graph :  
  
![For the graph:](assets/08F8C130-08A3-473B-A14F-B3465B2ED531.png)  
  
A Gaussian Process prior =  
“A distribution over possible functions, where any finite set of points follows a multivariate normal distribution”  
A Gaussian process is a collection (of an infinite number) of Gaussian random variables that have some joint multivariate gaussian distribution p(x1,x2,x3,...). There is literally nothing else to them, every single fact or technique involving them follows from this.  
The only thing that separates a gaussian process from a multivariate gaussian distribution is that the random variables in a gaussian process are indexed according to something like time or space. For example you might have a gaussian process written as X(t); this just means that each value of 't' indexes a distinct gaussian random variable X(t).  
This is all easier to understand by thinking in terms of discrete sets of random variables. A gaussian process is just the continuous limit of this.  
  
  
The arrow in "X → Y " signifies X has an effect on Y , or in other words, X is a cause of Y .  
  
  
A **Directed Acyclic Graph (DAG)** is:  
A graph with **directed edges (arrows)** and **no cycles**  
  
  
The core problem  
```
Individual effect = Y(1) − Y(0)

```
We only ever observe one of these. The other is the counterfactual — the world that didn't happen. This is what everything else is trying to reconstruct.  
ATE  
```
E[Y(1) − Y(0)]

```
Average effect across everyone. "What would happen if we ran this campaign for all users?"  
ATT  
```
E[Y(1)−Y(0) | T=1]

```
Effect only among those who were actually treated. "Did the campaign help the users who saw it?"  
ITT  
```
E[Y | assigned=1] − E[Y | assigned=0]

```
Effect of being assigned to treatment, regardless of whether people actually complied. The standard estimand in most business experiments.  
  
Why naive comparisons fail — selection bias  
E[Y|T=1] − E[Y|T=0] = ATE + Selection bias  
The raw difference in outcomes between exposed and unexposed conflates the true causal effect with pre-existing differences between the groups.  
Where selection bias comes from  
People who were exposed to the campaign are systematically different from those who weren't — they are younger, more active, more likely to subscribe anyway. The algorithm chose them for a reason. Any comparison that ignores this is mixing the causal effect of the campaign with the pre-existing advantages of the people it targeted.  
  
  
  
The key assumption for observational methods  
{ Y(0), Y(1) } ⊥ T | X  
Conditional independence — once you control for observed characteristics X, treatment assignment is as good as random. Also called unconfoundedness or selection on observables.  
  
METHOD  
CORE IDEA  
ASSUMPTION  
BREAKS WHEN  
Regression adjustment  
Add confounders as control variables. The coefficient on treatment captures variation unexplained by those controls.  
Linear relationship between confounders and outcome. All confounders measured.  
Unobserved confounder exists. Groups overlap so poorly that regression is extrapolating.  
Matching  
For each treated unit, find the most similar untreated unit. Compare outcomes within matched pairs. Discard unmatched units.  
All confounders measured. Enough untreated units exist to find close matches.  
Too many confounders (curse of dimensionality). Too few untreated units to match against.  
  
  
  
The curse of dimensionality refers to various phenomena that arise when analyzing and organizing data in high-dimensional spaces (often hundreds of dimensions) that do not occur in low-dimensional settings. As dimensions increase, data becomes sparse, making it harder to find patterns, causing distances between points to become indistinguishable, and leading to model overfitting  
  
**Difference-in-Differences (DiD) — the core idea**  
The problem with regression and matching was: people who were exposed to the campaign were fundamentally different people from those who weren't. We couldn't find a fair comparison.  
  
  
![Germany runs a Prime campaign in October. France does not. You have subscription rates for both countries](assets/F7CA011F-458F-4B68-8215-9A6951F2669B.png)  
  
  
**Synthetic control** solves this by building a custom "synthetic Germany" — a weighted blend of other countries that, together, match Germany's pre-campaign trajectory as closely as possible.  
  
No single country perfectly mirrors Germany. France has higher baseline rates. Spain has different seasonality. Italy has a different growth trend. But a carefully chosen blend — 40% France + 35% Netherlands + 25% Italy — might track Germany almost perfectly in the pre-campaign period. Once that blend is built, you use it as the counterfactual for what Germany would have looked like without the campaign.  
  
  
**Layer 2 — The parallel trends assumption in depth**  
  
  
  
```
E[Y(0)_post − Y(0)_pre | Treated] = E[Y(0)_post − Y(0)_pre | Control]

```
In the absence of treatment, the treated group would have followed the same trend as the control group
