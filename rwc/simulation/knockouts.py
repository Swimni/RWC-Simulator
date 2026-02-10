# def generer_huitiemes(premiers, deuxiemes, troisiemes):
# 	troisiemes = sorted(troisiemes, key=lambda x: x["points"], reverse=True)[:4]

# 	return [
# 		(premiers["A"], troisiemes[3]["team"]),
# 		(premiers["B"], troisiemes[2]["team"]),
# 		(premiers["C"], troisiemes[1]["team"]),
# 		(premiers["D"], troisiemes[0]["team"]),
# 		(premiers["E"], deuxiemes["D"]),
# 		(premiers["F"], deuxiemes["B"]),
# 		(deuxiemes["A"], deuxiemes["E"]),
# 		(deuxiemes["F"], deuxiemes["C"]),
# 	]

from simulation.matches import simuler_match

def generer_huitiemes(premiers, deuxiemes, troisiemes):
    troisiemes = sorted(troisiemes, key=lambda x: x["points"], reverse=True)[:4]

    return [
        (premiers["A"], troisiemes[3]["team"]),
        (premiers["B"], troisiemes[2]["team"]),
        (premiers["C"], troisiemes[1]["team"]),
        (premiers["D"], troisiemes[0]["team"]),
        (premiers["E"], deuxiemes["D"]),
        (premiers["F"], deuxiemes["B"]),
        (deuxiemes["A"], deuxiemes["E"]),
        (deuxiemes["F"], deuxiemes["C"]),
    ]

# ----------------------
# Fonction générique pour simuler un tour
# ----------------------
def simuler_tour(matchs, teams, tour="Tour"):
    print(f"\n🏉 {tour} :\n")
    gagnants = []
    for i, (a, b) in enumerate(matchs, 1):
        g, p, prob, bonus = simuler_match(a, b, teams)
        print(f"Match {i} : {a} vs {b} → {g} gagne (p={prob:.2f})")
        gagnants.append(g)
    return gagnants

# ----------------------
# Quarts de finale
# ----------------------
def generer_quarts(huitiemes, teams):
    quarts = [
        (huitiemes[0][0], huitiemes[1][0]),  # gagnants match1 vs match2
        (huitiemes[7][0], huitiemes[4][0]),  # gagnants match8 vs match5
        (huitiemes[6][0], huitiemes[5][0]),  # gagnants match7 vs match6
        (huitiemes[2][0], huitiemes[3][0]),  # gagnants match3 vs match4
    ]
    return simuler_tour(quarts, teams, tour="Quarts de finale")

# ----------------------
# Demi-finales
# ----------------------
def generer_demies(gagnants_quarts, teams):
    demies = [
        (gagnants_quarts[0], gagnants_quarts[1]),
        (gagnants_quarts[2], gagnants_quarts[3])
    ]
    return simuler_tour(demies, teams, tour="Demi-finales")

# ----------------------
# Finale
# ----------------------
def generer_finale(gagnants_demies, teams):
    finale = [(gagnants_demies[0], gagnants_demies[1])]
    gagnant = simuler_tour(finale, teams, tour="Finale")
    print(f"\n🏆 Champion : {gagnant[0]}")
    return gagnant[0]
