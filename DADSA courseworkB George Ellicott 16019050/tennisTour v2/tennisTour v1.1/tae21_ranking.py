class tae21_ranking:
    def __init__(self, player, ranking, prizeMoney):
        self._name = player
        self._ranking = ranking
        self._prizeMoney = prizeMoney

    def get_player(self):
        return self._name

    def get_ranking(self):
        return self._ranking

    def get_prizeMoney(self):
        return self._prizeMoney

    def __str__(self):
        return '({0}, {1}, {2}, {3})'.format(self._name, self._ranking, self._prizeMoney)
