
Decision-Aware Probabilistic Supply Chain Delay System
====================================================

This project predicts ETA uncertainty using quantile regression and makes cost-optimal routing decisions.

Key Principle:
Prediction is useless unless tied to decisions and cost.

Flow:
Signals → Features → Quantile ETA → Expected Cost → Decision

Metrics:
Cost, Regret, Overconfidence (not RMSE)

Tech:
Python, Pandas, NumPy, LightGBM, FastAPI
