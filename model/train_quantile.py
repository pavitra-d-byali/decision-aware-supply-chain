
import lightgbm as lgb

def train(X, y, q):
    params = {
        "objective": "quantile",
        "alpha": q,
        "learning_rate": 0.05,
        "num_leaves": 31
    }
    return lgb.train(params, lgb.Dataset(X, y), num_boost_round=200)
