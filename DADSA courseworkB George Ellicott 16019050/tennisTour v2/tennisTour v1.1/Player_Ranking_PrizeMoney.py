class Player_Ranking_PrizeMoney:
    def __init__(self, player, ranking, prizeMoney, bonus):
        self._name = player
        self._ranking = ranking
        self._prizeMoney = prizeMoney
        self._scoreBonus = bonus
        
        
    def get_player(self):
        return self._name

    def get_ranking(self):
        return self._ranking
    
    def get_prizeMoney(self):
        return self._prizeMoney

    def get_scoreDiff(self):
        return self._scoreBonus
    
    def __str__(self):
        return '({0}, {1}, {2}, {3})'.format(self._name, self._ranking, self._prizeMoney, self._scoreBonus)
