
def expected_cost(p_delay, sla_penalty, intervention_cost):
    return p_delay * sla_penalty + intervention_cost
