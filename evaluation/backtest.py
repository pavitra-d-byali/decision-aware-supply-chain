
def backtest(y_true, p90, sla=24, penalty=100, reroute_cost=20):
    cost = 0
    for yt, p in zip(y_true, p90):
        if p > sla:
            cost += reroute_cost
        elif yt > sla:
            cost += penalty
    return cost
