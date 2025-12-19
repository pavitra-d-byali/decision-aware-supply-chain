
import numpy as np
import pandas as pd

def simulate_shipments(n=50000, seed=42):
    rng = np.random.default_rng(seed)
    distance = rng.uniform(50, 2000, n)
    traffic = rng.gamma(2.0, 1.5, n)
    weather = rng.beta(2, 5, n) * 10
    congestion = rng.normal(0.5, 0.15, n).clip(0, 1)

    stress = 0.3*traffic + 0.4*weather + 0.5*congestion + 0.0005*distance
    base_eta = distance / 60
    noise = rng.lognormal(0, 0.3, n)
    true_eta = base_eta * (1 + stress * noise)

    latency = rng.exponential(5 + 10*stress)
    df = pd.DataFrame({
        "distance_km": distance,
        "traffic_index": traffic,
        "weather_severity": weather,
        "hub_congestion": congestion,
        "data_latency_min": latency,
        "true_eta": true_eta
    })

    mask = rng.random(n) < (0.1 + 0.3*stress)
    df.loc[mask, "traffic_index"] = np.nan
    return df
