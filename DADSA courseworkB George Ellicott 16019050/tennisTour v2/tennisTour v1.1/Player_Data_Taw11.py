class Player_Data_Taw11:
    def __init__(self,player, wins, wins_three_score_bonus, wins_two_score_bonus, wins_one_score_bonus, losses):

        self._player = player
        self._wins = wins
        self._win_by_three = wins_three_score_bonus
        self._win_by_two = wins_two_score_bonus
        self._win_by_one = wins_one_score_bonus
        self._losses = losses

    def get_player(self):
        return self._player

    def get_wins(self):
        return self._wins

    def get_win_by_three(self):
        return self._win_by_three

    def get_win_by_two(self):
        return self._win_by_two

    def get_win_by_one(self):
        return self._win_by_one

    def get_loses(self):
        return self._losses

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self._player, self._wins, self._win_by_three, self._win_by_two, self._win_by_one, self._losses)
