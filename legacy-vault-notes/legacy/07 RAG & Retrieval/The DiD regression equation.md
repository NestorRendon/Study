# The DiD regression equation

```
Y_it = α + β·Treated_i + γ·Post_t + δ·(Treated_i × Post_t) + ε_it
Y_it

```
Outcome for unit i at time t — e.g. subscription rate for country i in week t  
```
α

```
Baseline level — the control group's outcome in the pre period  
```
β · Treated_i

```
How much the treated group differs from control on average, before treatment. Captures pre-existing level differences. β = 1 if Germany, 0 if France.  
```
γ · Post_t

```
How much both groups change from pre to post — the shared time trend. γ = 1 after campaign launch, 0 before.  
δ · (Treated × Post)  
This is the DiD estimator. The coefficient on the interaction term. It captures the extra change in the treated group, above and beyond the shared time trend. δ is your causal estimate.
