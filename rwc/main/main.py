import json
from simulation.pools import simuler_poule
from simulation.knockouts import (
    generer_huitiemes,
    generer_quarts,
    generer_demies,
    generer_finale
)

def main():
    # Chargement des données
    with open("data/teams.json") as f:
        teams = json.load(f)

    with open("data/pools.json") as f:
        pools = json.load(f)

    premiers = {}
    deuxiemes = {}
    troisiemes = []

    # Simulation des poules
    for nom_poule, poule in pools.items():
        scores, premier, deuxieme, troisieme = simuler_poule(
            nom_poule,
            poule,
            teams
        )

        premiers[nom_poule] = premier
        deuxiemes[nom_poule] = deuxieme

        troisiemes.append({
            "team": troisieme,
            "points": scores[troisieme]
        })

    # Huitièmes de finale
    huitiemes = generer_huitiemes(premiers, deuxiemes, troisiemes)
    print("\n🏉 Huitièmes de finale :\n")
    for i, (a, b) in enumerate(huitiemes, 1):
        print(f"Match {i} : {a} vs {b}")

    # Quarts de finale
    gagnants_quarts = generer_quarts(huitiemes, teams)

    # Demi-finales
    gagnants_demies = generer_demies(gagnants_quarts, teams)

    # Finale
    champion = generer_finale(gagnants_demies, teams)


if __name__ == "__main__":
    main()
