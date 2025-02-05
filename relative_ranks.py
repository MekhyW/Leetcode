class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for player in score:
            player_rank = sorted_score.index(player) + 1
            if player_rank <= 3:
                score[score.index(player)] = ranks[player_rank - 1]
            else:
                score[score.index(player)] = str(player_rank)
        return score