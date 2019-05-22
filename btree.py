from board import Board
from binarynode import BinaryNode


class Tree:
    """
    BinaryTree, having the same functionality as Tree, but performing
    less computations and less precise (only 2 options)
    """
    def __init__(self):
        """
        initialise the tree (tree calculates 2 possible options till end)
        """
        self.board = Board()
        self.root = BinaryNode(Board(), None, Board.PLAYER_1)
        self.player = Board.PLAYER_0
        self.winner = None

    def move(self, position):
        """ Perform a move as a player """

        if self.board[position] != Board.CELL_EMPTY:
            raise ValueError('Not empty cell')

        self.board[position] = self.player
        self.root = BinaryNode(self.board, position, self.player)

        self.change_player()

    def get_move(self):
        """ Get a move from computer """
        if self.root.children is None:
            raise ValueError('End of the game')

        # sort to choose next node with the highest probability of winning (highest scores)
        children = [*sorted(self.root.children, key=
                    lambda x: x.scores[Board.PLAYERS.index(self.player)])]

        self.root = children[0]  # child with the lowest score (distance from winning)
        self.board[self.root.position] = self.player
        self.change_player()

    def change_player(self):
        """ After move setup - player change and win calculations """
        if self.root.children is None:
            if self.root.scores[0] == 0:
                self.winner = Board.PLAYER_0
            elif self.root.scores[1] == 0:
                self.winner = Board.PLAYER_1
            elif self.root.scores[0] == 1 and self.root.scores[1] == 1:
                self.winner = 'draw'

        self.player = Board.PLAYERS[(Board.PLAYERS.index(self.player) + 1) %
                                    len(Board.PLAYERS)]
