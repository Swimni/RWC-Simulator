def prob_victoire(team_a, team_b, teams):
	elo_a = teams[team_a]["elo"]
	elo_b = teams[team_b]["elo"]
	return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))