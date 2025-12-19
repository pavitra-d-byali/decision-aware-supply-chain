
from decision.cost import expected_cost

def decide(p90_eta, sla, sla_penalty=100, reroute_cost=20):
    p_delay = float(p90_eta > sla)
    stay = expected_cost(p_delay, sla_penalty, 0)
    reroute = expected_cost(0.1, sla_penalty, reroute_cost)
    return "reroute" if reroute < stay else "stay"
