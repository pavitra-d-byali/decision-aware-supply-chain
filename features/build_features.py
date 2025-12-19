
def build_features(df):
    df = df.copy()
    df["traffic_weather_interaction"] = df["traffic_index"] * df["weather_severity"]
    df["stress_score"] = df["traffic_weather_interaction"].fillna(0) + df["hub_congestion"]
    df["uncertainty_multiplier"] = 1 + 0.01 * df["data_latency_min"]
    df.fillna(df.median(), inplace=True)
    return df
