import json

# 1. Importer le fichier json et le lire
with open('./data/players.json') as f:
    players:list[dict] = json.load(f)

# 2. Trier les joueurs en fonction de leur elo_points
players_sorted:list[dict] = sorted(players,     
                                   key=lambda player: player['elo_points'])

# 3. Faire les deux groupes
nbr_players:int = len(players)
group_1:list[dict] = players_sorted[:nbr_players//2]
group_2:list[dict] = players_sorted[nbr_players//2:]

# Confrontations
battles:list = []
for i in range(nbr_players//2):
    battle:list[dict, dict] = [group_1[i], group_2[i]]
    battles.append(battle)

# Ecrire les confrontations dans un nouveau fichier json
with open('./data/battles.json', 'w') as f:
    json.dump(battles, f, indent=4)

