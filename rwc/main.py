import json
import random

with open("data/teams.json") as f:
	teams = json.load(f)

with open("data/pools.json") as f:
	pools = json.load(f)

def prob_victoire(team_a, team_b):
	elo_a = teams[team_a]["elo"]
	elo_b = teams[team_b]["elo"]
	return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

def simuler_poule_fixe(nom_poule, poule):
	scores = {team: 0 for team in poule}

	print(f"\nPoule {nom_poule} : {', '.join(poule)}\n")

	for i in range(len(poule)):
		for j in range(i + 1, len(poule)):
			team_a, team_b = poule[i], poule[j]
			p = prob_victoire(team_a, team_b)

			if random.random() < p:
				gagnant = team_a
				perdant = team_b
			else:
				gagnant = team_b
				perdant = team_a

			scores[gagnant] += 4

			if 0.42 <= p <= 0.58:
				scores[perdant] += 1

			print(f"{team_a} vs {team_b} → {gagnant} gagne ! "
				f"Points: {team_a}={scores[team_a]}, {team_b}={scores[team_b]} ; P = {p:.2f}")

	classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)

	print("\nClassement final :")
	for rank, (team, score) in enumerate(classement, 1):
		print(f"{rank}. {team} - {score} points")

	premier = classement[0][0]
	deuxieme = classement[1][0]

	return scores, premier, deuxieme

if __name__ == "__main__":
	for nom_poule, poule in pools.items():
		simuler_poule_fixe(nom_poule, poule)
