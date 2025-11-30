class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
    
    @classmethod
    def score_to_string(cls, score: int) -> str | None:
        score_map = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_map.get(score, "Unknown")

    def get_score(self) -> str:
        score = ""

        if self.player1_score == self.player2_score:
            if self.player1_score > 2:
                score = "Deuce"
            else:
                score = f"{self.score_to_string(self.player1_score)}-All"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            player1_lead = self.player1_score - self.player2_score

            if player1_lead == 1:
                score = "Advantage player1"
            elif player1_lead == -1:
                score = "Advantage player2"
            elif player1_lead >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = f"{self.score_to_string(self.player1_score)}-{self.score_to_string(self.player2_score)}"

        return score
