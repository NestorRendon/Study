# 8. Gradient Problems & Fixes

| Problem | Symptom | Fix |
| ------------------ | ------------------------ | -------------------------------------- |
| Vanishing gradient | Early layers don't learn | ReLU, residual connections, LSTM gates |
| Exploding gradient | Loss goes to NaN | Gradient clipping (clip_grad_norm) |
| Dying ReLU | Neurons output 0 forever | Leaky ReLU, ELU, proper init |
| Saddle points | Training stalls | Momentum, Adam |
