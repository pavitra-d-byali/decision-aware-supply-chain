
import pickle
from data.simulate import simulate_shipments
from features.build_features import build_features
from model.train_quantile import train

df = simulate_shipments()
y = df["true_eta"]
X = build_features(df.drop(columns=["true_eta"]))

models = {q: train(X, y, q) for q in [0.5, 0.9, 0.99]}

with open("models.pkl", "wb") as f:
    pickle.dump(models, f)
