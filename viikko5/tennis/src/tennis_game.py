class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def add_point(self, player_name: str):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        elif player_name == self.player2_name:
            self.player2_score = self.player2_score + 1
        else:
            raise ValueError("Unknown player name")

    @classmethod
    def score_to_string(cls, score: int) -> str | None:
        score_map = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_map.get(score, "Unknown")

    def get_score(self) -> str:
        if self.player1_score == self.player2_score and self.player1_score >= 3:
            return "Deuce"

        if self.player1_score >= 4 or self.player2_score >= 4:
            score_diff = self.player1_score - self.player2_score
            if abs(score_diff) == 1:
                return "Advantage " + (self.player1_name if score_diff > 0 else self.player2_name)
            else:
                return "Win for " + (self.player1_name if score_diff > 0 else self.player2_name)

        score = f"{self.score_to_string(self.player1_score)}-"
        if self.player1_score == self.player2_score:
            score += "All"
        else:
            score += self.score_to_string(self.player2_score)
        return score
