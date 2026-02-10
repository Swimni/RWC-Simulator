import random
from simulation.probabilities import prob_victoire

def simuler_match(team_a, team_b, teams):
	p = prob_victoire(team_a, team_b, teams)

	if p >= 0.85:
		return team_a, team_b, p, 1
	if p <= 0.15:
		return team_b, team_a, p, 1

	if random.random() < p:
		return team_a, team_b, p, 0
	return team_b, team_a, p, 0
