from board import Board
import random


class BinaryNode:
    NUM_CHILDREN = 2

    def __init__(self, board, position, current_player):

        self.board = board
        self.position = position
        self.current_player = current_player  # character x /" "/ o
        # scores is minimal number of steps from wining for each player at current state of board
        self.scores = [None, None]  # sores[0] scores of 0 player, scores[1] - scores of 1 player
        self.children = None  # list of children (left, right)

        self.calculate_scores()

    def left(self):
        try:
            node = self.children[0]
        except IndexError:
            raise IndexError("No left node")
        return node

    def right(self):
        try:
            node = self.children[1]
        except IndexError:
            raise IndexError("No right node")
        return node

    def add_left(self, value):
        if not self.left_exists():
            self.children = [value]

    def add_right(self, value):
        if not self.right_exists():
            self.children.append(value)

    def left_exists(self):
        if self.children and len(self.children) >= 1:
            return True
        else:
            return False

    def right_exists(self):
        if self.children and len(self.children) >= 2:
            return True
        else:
            return False

    def calculate_scores(self):
        """
        Calculate the number of steps to take to the winning from current stage
        """
        win = self.board.winner()
        if win == Board.CELL_X:
            self.scores = [0, 1]  # 0 steps to winning (because won)
        elif win == Board.CELL_0:
            self.scores = [1, 0]
        elif win == Board.CELL_EMPTY and self.board.is_full():
            self.scores = [1, 1]
        else:
            self.add_children()

    def add_children(self):
        """
        Add children and calculate scores
        """
        self.children = []
        # get player to understand whose step to predict (bot or player)
        player = Board.PLAYERS[(Board.PLAYERS.index(self.current_player) + 1) % len(Board.PLAYERS)]

        num_children = 0
        random_steps = list(range(9))
        random.shuffle(random_steps)
        # choose 2 (NUM_CHILDREN) of 9 random steps to append
        for i in random_steps:
            if self.board[i] == Board.CELL_EMPTY and \
                    num_children < self.NUM_CHILDREN:
                # create new node with board
                new_board = self.board.get_copy()
                new_board[i] = player
                if num_children == 0:
                    self.add_left(BinaryNode(new_board, i, player))
                if num_children == 1:
                    self.add_right(BinaryNode(new_board, i, player))
                num_children += 1

        cur_ind = self.board.PLAYERS.index(self.current_player)

        # choose the least distant state from winning state
        # here we calculate the distance by adding 1 to the lowest distance of children to the win
        self.scores[cur_ind] = min(self.children, key=lambda x: x.scores[cur_ind]).scores[cur_ind] + 1

        self.scores[(cur_ind + 1) % 2] = min(self.children,
                                             key=lambda x: x.scores[(cur_ind + 1) % 2]).scores[(cur_ind + 1) % 2] + 1

