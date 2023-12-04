class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.score = ""
        self.tennis_words = ["Love", "Fifteen", "Thirty", "Forty"]


    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1


    def get_score(self):
        if self.player1_points == self.player2_points:
            if self.player1_points <= 2:
                self.score = f"{self.tennis_words[self.player1_points]}-All"
            else:
                self.score = "Deuce"
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self. player2_points

            if minus_result == 1:
                self.score = "Advantage player1"
            elif minus_result == -1:
                self.score = "Advantage player2"
            elif minus_result >= 2:
                self.score = "Win for player1"
            else:
                self.score = "Win for player2"
        else:
            self.score = f"{self.tennis_words[self.player1_points]}-{self.tennis_words[self.player2_points]}"

        return self.score
