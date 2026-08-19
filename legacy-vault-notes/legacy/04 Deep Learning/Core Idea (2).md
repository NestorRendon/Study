# Core Idea

Find the hyperplane that separates classes with the **maximum margin** — the widest possible gap between the two classes. Only the points closest to the boundary matter — these are the **support vectors**.  
  
  
Maximize:   margin = 2 / ‖w‖  
Subject to: yᵢ(w·xᵢ + b) ≥ 1   for all i  
**ELI5:** Draw a line between two groups. Now push that line as far as possible from both groups until it's perfectly centered in the gap. The margin is that gap width.
