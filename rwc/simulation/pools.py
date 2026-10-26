from simulation.matches import simuler_match

def afficher_classement(scores):
	classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	for i, (team, pts) in enumerate(classement, 1):
		print(f"{i}. {team} - {pts} pts")
	print()

def simuler_poule(nom_poule, poule, teams):
	scores = {team: 0 for team in poule}

	print(f"\n🏉 Poule {nom_poule} : {', '.join(poule)}\n")

	for i in range(len(poule)):
		for j in range(i + 1, len(poule)):
			a = poule[i]
			b = poule[j]

			gagnant, perdant, prob, bonus = simuler_match(a, b, teams)

			scores[gagnant] += 4 + bonus
			if 0.42 <= prob <= 0.58:
				scores[perdant] += 1

			print(
				f"{a} vs {b} → {gagnant} gagne "
				f"(p={prob:.2f}, bonus={bonus})"
			)

	print("\nClassement :")
	afficher_classement(scores)

	classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)

	return (
		scores,
		classement[0][0],
		classement[1][0],
		classement[2][0],
	)
