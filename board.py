class Board:
    CELL_EMPTY = ' '
    CELL_X = 'x'
    CELL_0 = 'o'
    CELLS = [CELL_EMPTY, CELL_X, CELL_0]

    PLAYER_0 = 'x'
    PLAYER_1 = 'o'
    PLAYERS = [PLAYER_0, PLAYER_1]

    def __init__(self, values=None):

        if values is None:
            values = self.CELL_EMPTY * 9
        if not all(map(lambda x: x in self.CELLS, values)):
            raise ValueError('One of the values is invalid')

        self._cells = [c for c in values]

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise ValueError('Index should be integer')
        if not 0 <= i < 10:
            raise IndexError('Index should be between 0 and 10')
        return self._cells[i]

    def __setitem__(self, i, val):
        if not isinstance(i, int):
            raise ValueError('Index should be integer')
        if not 0 <= i < 10:
            raise IndexError('Index should be between 0 and 10')
        self._cells[i] = val

    def get_copy(self):
        """
        Copy a board to avoid changing original
        """
        new_board = Board()
        for i in range(9):
            new_board[i] = self[i]
        return new_board

    def winner(self):
        """
        Returns the winner or empty cell
        """

        combinations = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2),
                        (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]

        for combination in combinations:
            if self[combination[0]] == self[combination[1]] == self[combination[2]]:
                if self[combination[0]] != self.CELL_EMPTY:
                    return self[combination[0]]
        return self.CELL_EMPTY

    def is_full(self):
        for cell in self._cells:
            if cell == self.CELL_EMPTY:
                return False
        return True

    def __str__(self):
        result = '-----\n'
        for i in range(3):
            result += '|' + self[i*3] + self[i*3+1] + self[i*3+2] + '|\n'
        result += '-----'
        return result
