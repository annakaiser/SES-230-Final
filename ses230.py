#!/usr/bin/env python
# coding: utf-8

# In[27]:


#simulate a ping pong match with the question of "what is the avg amount of times the ball goes back and forth
#before someone loses the round
#players from Carolina Gold Rush and Princeton Revolution in the Table Tennis League
import random

class Player:
    def __init__(self, name, singles_win, singles_loss, singles_percentage,
                 doubles_win, doubles_loss, doubles_percentage,
                 golden_game_pf, golden_game_pa, golden_game_percentage, power_ranking):
        self.name = name
        self.singles_win = singles_win
        self.singles_loss = singles_loss
        self.singles_percentage = singles_percentage / 100.0
        self.doubles_win = doubles_win
        self.doubles_loss = doubles_loss
        self.doubles_percentage = doubles_percentage / 100.0
        self.golden_game_pf = golden_game_pf
        self.golden_game_pa = golden_game_pa
        self.golden_game_percentage = golden_game_percentage / 100.0
        self.power_ranking = power_ranking

def simulate_singles_match(player1, player2, games):
    player1_wins = 0
    player2_wins = 0
    total_hits = 0

    for _ in range(games):
        hits = simulate_game(player1, player2)
        total_hits += hits
        winner = player1 if hits % 2 == 0 else player2

        if winner == player1:
            player1_wins += 1
        else:
            player2_wins += 1

    average_hits_per_round = total_hits / (games * 1.0)
    return player1_wins, player2_wins, average_hits_per_round

def simulate_game(player1, player2):
    ball_count = 0

    while True:
        ball_count += 1

        if random.random() < player1.singles_percentage:
            return ball_count
        elif random.random() < player2.singles_percentage:
            return ball_count

def main():
    #players for Carolina Gold Rush
    enzo_angeles = Player("Enzo Angeles", 20, 7, 74.1, 21, 6, 77.8, 39, 27, 64.4, 796.5)
    hong_lin = Player("Hong Lin", 0, 3, 0, 19, 5, 77.8, 29, 16, 64.4, 757.9)
    kai_zhang = Player("Kai Zhang", 10, 8, 55.6, 0, 0, 0, 23, 20, 53.5, 707.1)
    romain_lorentz = Player("Romain Lorentz", 14, 13, 51.9, 0, 0, 0, 25, 30, 45.5, 688.8)
    bastien_dupont = Player("Bastien Dupont", 4, 5, 44.4, 2, 1, 66.7, 14, 16, 46.7, 680.0)
    jeremy_hazin = Player("Jeremy Hazin", 7, 11, 38.9, 0, 0, 0, 21, 19, 52.5, 652.8)
    peter_kostovski = Player("Peter Kostovski", 0, 6, 0, 0, 0, 0, 6, 6, 50, "NQ")

    #players for Princeton Revolution
    kanamitsu_koyo = Player("Kanamitsu Koyo", 9, 6, 60, 0, 0, 0, 19, 10, 65.5, 754.5)
    levgen_pryshchepa = Player("Levgen Pryshchepa", 14, 7, 66.7, 1, 2, 33.3, 20, 28, 0, 707.8)
    jinxin_wang = Player("Jinxin Wang", 8, 13, 38.1, 0, 0, 0, 26, 21, 55.3, 683.5)
    jishan_liang = Player("Jishan Liang", 9, 9, 50, 4, 8, 33.3, 20, 25, 44.4, 671.4)
    angela_guan = Player("Angela Guan", 0, 0, 0, 9, 18, 33.3, 21, 39, 35, 581)
    alexander_chen = Player("Alexander Chen", 3, 3, 50, 0, 0, 0, 5, 7, 41.7, "NQ")

    #simulate singles matches
    singles_results = []
    average_hits_per_round_list = []
    players_cg = [enzo_angeles, hong_lin, kai_zhang, romain_lorentz, bastien_dupont, jeremy_hazin, peter_kostovski]
    players_pr = [kanamitsu_koyo, levgen_pryshchepa, jinxin_wang, jishan_liang, angela_guan, alexander_chen]

    for player1, player2 in zip(players_cg, players_pr):
        player1_wins, player2_wins, average_hits_per_round = simulate_singles_match(player1, player2, 3)
        singles_results.append((player1_wins, player2_wins))
        average_hits_per_round_list.append(average_hits_per_round)

    #print results
    print("Singles Match Results:")
    for i, (player1_wins, player2_wins) in enumerate(singles_results):
        print(f"{players_cg[i].name} vs {players_pr[i].name}: {player1_wins} - {player2_wins}")
        print(f"Average hits per round for {players_cg[i].name} vs {players_pr[i].name}: {average_hits_per_round_list[i]:.2f}")

if __name__ == "__main__":
    main()


# In[ ]:




