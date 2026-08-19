# Neural Network, RNN and LSTM Metrics

**Prev:** [[04 - Object Detection and Segmentation Metrics]] · **Next:** [[06 - LLM and Generative Text Metrics]]

---

## Interview one-liner

Before asking "is the model good," a neural network needs a separate, earlier question answered: "**is training even working**?" That's a different set of signals — loss curves, gradient health, calibration — on top of whatever task metric (accuracy, F1, perplexity) you'd report at the end.

---

## In plain English

A neural net can have a perfectly reasonable final accuracy number and still have been trained badly (got lucky, overfit then got saved at the right checkpoint, etc.), or have a mediocre final number while actually still improving when training was cut short. The metrics in this note are about **diagnosing the training process itself**, plus the handful of metrics that are specific to sequence models like RNNs/LSTMs, which classic classification/regression metrics don't cover.

---

## Reading the loss curve

| Pattern | What it means | What to do |
|---------|-------------------|--------------|
| Train loss ↓, val loss ↓, both flattening together | Healthy training, converging | Maybe stop soon, or fine, keep going |
| Train loss ↓, val loss ↑ (diverging) | **Overfitting** — see [[05 Deep Learning/01 - Bias-Variance Tradeoff]] | Regularization, dropout, early stopping, more data |
| Both loss curves stay high, flat | **Underfitting** — model too small, learning rate wrong, or a bug | Bigger model, tune LR, check data pipeline |
| Loss spikes or goes to NaN | Learning rate too high, or exploding gradients | Gradient clipping, lower LR — see [[05 Deep Learning/13 - Diagnosing Neural Network Failures]] |

---

## Top-K accuracy

$$\text{Top-K Accuracy} = \frac{1}{n}\sum_{i=1}^n \mathbb{1}\left[y_i \in \text{top-K predictions}_i\right]$$

Instead of asking "was the single highest-probability class correct," ask "was the correct class in the model's top $K$ guesses." Standard for large-output-space problems (e.g. ImageNet's 1000 classes — Top-5 accuracy is a classic benchmark number) where being *close* still has value, e.g. for a human reviewing a shortlist.

---

## Calibration — is the model's *confidence* trustworthy?

A model can be accurate but **overconfident** — saying "95% sure" when it's actually right only 70% of the time. This matters anywhere a downstream decision depends on the probability, not just the label (e.g. deciding whether to auto-approve vs escalate to a human).

$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$

Bin predictions into $M$ confidence buckets $B_m$ (e.g. 0-10%, 10-20%, ...). For each bucket, compare the **actual accuracy** of predictions in that bucket against their **average stated confidence**. A perfectly calibrated model has $\text{ECE} = 0$: when it says "70% confident," it's right 70% of the time.

---

## Perplexity — the general form

Perplexity shows up for any model that predicts a probability distribution over the next token/class in a sequence (language models, but also any sequence-labeling RNN/LSTM):

$$\text{Perplexity} = \exp\left(-\frac{1}{N}\sum_{i=1}^N \log P(x_i \mid x_{<i})\right)$$

It's literally $e$ raised to the average cross-entropy loss — interpretable as **"the model is as confused as if it were choosing uniformly among this many options at each step."** Lower is better; perplexity of 1 means perfectly confident and correct every time. *Full treatment, with the LLM-specific interpretation, is in [[06 - LLM and Generative Text Metrics]].*

---

## What's specific to RNN / LSTM evaluation

| Consideration | Why it's different from a plain classifier |
|------------------|--------------------------------------------|
| **Token-level vs sequence-level accuracy** | A sequence can be 90% correct token-by-token and still be a completely wrong sentence — decide which granularity actually matters for your task |
| **Teacher forcing during training vs free-running at inference** | During training the model sees the *true* previous token; at inference it sees its *own* (possibly wrong) previous prediction — a model can look great on training-time metrics and still drift/compound errors at real inference time (**exposure bias**) |
| **Gradient norm over time** | RNNs/LSTMs are prone to vanishing/exploding gradients across long sequences — monitoring the gradient norm during training (not just the loss) catches this before the loss curve even looks wrong. LSTMs' gating mechanism specifically exists to fight vanishing gradients — see [[05 Deep Learning/11 - RNN LSTM and GRU]] |
| **Sequence-level metrics (BLEU, edit distance)** | For seq2seq output (translation, summarization) you need metrics that compare whole generated sequences, not per-token accuracy — covered in [[06 - LLM and Generative Text Metrics]] |

---

## Common traps

| Trap | Why it's wrong | What to say instead |
|------|------------------|----------------------|
| Judging a model only by final validation accuracy | Says nothing about *how* training went — could've been one lucky checkpoint | "I'd look at the full loss curve, not just the final number, to catch overfitting or instability" |
| Trusting a model's stated confidence at face value | Neural nets are frequently overconfident, especially after training with cross-entropy for many epochs | "I'd check calibration (ECE) or use temperature scaling before trusting the probabilities for a real decision" |
| Evaluating an RNN/LSTM only with teacher forcing | Training-time metrics with teacher forcing hide exposure bias | "I'd also evaluate free-running (using the model's own predictions as input) since that's what happens at real inference time" |
| Ignoring gradient norms when training a deep/recurrent net | The loss can look "stuck" for a while before you realize gradients vanished or exploded | "I'd log the gradient norm alongside the loss to catch this earlier" |

---

**Next:** [[06 - LLM and Generative Text Metrics]]
