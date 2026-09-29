class Scoreboard:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def update_score(self, result):

        if result == "Win":
            self.wins += 1

        elif result == "Loss":
            self.losses += 1

        elif result == "Draw":
            self.draws += 1

    def get_total_games(self):
        return self.wins + self.losses + self.draws

    def get_win_percentage(self):

        total_games = self.get_total_games()

        if total_games == 0:
            return 0

        return (self.wins / total_games) * 100

    def display_scoreboard(self):

        print("\n========== SCOREBOARD ==========")
        print("Wins   :", self.wins)
        print("Losses :", self.losses)
        print("Draws  :", self.draws)
        print("Games  :", self.get_total_games())
        print("Win %  :", round(self.get_win_percentage(), 2))
        print("================================")