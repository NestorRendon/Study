# One more thing — what Anthropic does differently

Instead of pure RLHF, Anthropic uses **Constitutional AI (CAI)** for Claude:  
  
  
RLHF:  
human raters evaluate responses → reward model → train main model  
  
Constitutional AI:  
1. Define a "constitution" — a set of principles  
   ("be helpful", "avoid harm", "be honest"...)  
  
2. Model critiques its OWN responses against the constitution  
  
3. Model revises its own responses  
  
4. Revised responses used as training data  
  
5. Reward model trained on AI feedback, not just human feedback  
  
  
  
GPT (OpenAI):  
Random weights  
      ↓  
Pretraining (raw text, trillions of tokens)  
      ↓  
SFT (human written conversations, ~13k examples)  
      ↓  
Reward model training (human preference pairs, ~33k examples)  
      ↓  
PPO optimization (RL against reward model + KL penalty)  
      ↓  
ChatGPT / GPT-4  
  
  
Claude (Anthropic):  
Random weights  
      ↓  
Pretraining (raw text, trillions of tokens)  
      ↓  
SFT (human written conversations)  
      ↓  
SL-CAI (model critiques and revises its own outputs  
         using constitution → new SFT data)  
      ↓  
RLAIF (model labels preferences using constitution  
        → reward model trained on AI feedback)  
      ↓  
PPO optimization (RL against reward model + KL penalty)  
      ↓  
Claude  
  
The Reason and Act (ReAct) framework solves this by interleaving these two capabilities.
