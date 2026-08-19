# Pros & Cons of MoE

| Pros | Cons |
| ----------------------------------------------- | ---------------------------------------------- |
| Massive capacity at low inference cost | High memory — all experts must be loaded |
| Specialization — experts learn different skills | Training instability, routing collapse risk |
| Scales well with more experts | Communication overhead in distributed training |
| State of the art efficiency | Harder to fine-tune than dense models |
