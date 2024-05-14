players_pool = {}

data = input()
while data != "Season end":
    if "->" in data:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if player not in players_pool.keys():
            players_pool[player] = {position: skill}
        else:
            if position not in players_pool.values():
                players_pool[player][position] = skill
            else:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill
    elif "vs" in data:
        first_player, second_player = data.split(" vs ")
        if first_player in players_pool.keys() and second_player in players_pool.keys():
            common_positions = set(players_pool[first_player].keys() & players_pool[second_player].keys())
            if len(common_positions) > 0:
                for position in common_positions:
                    if players_pool[first_player][position] == players_pool[second_player][position]:
                        continue
                first_player_total_skill = sum(players_pool[first_player].values())
                second_player_total_skill = sum(players_pool[second_player].values())
                if first_player_total_skill > second_player_total_skill:
                    del players_pool[second_player]
                elif second_player_total_skill > first_player_total_skill:
                    del players_pool[first_player]
    data = input()


for player, positions in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(positions.values())} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
