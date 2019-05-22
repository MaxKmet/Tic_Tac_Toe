from btree import Tree as BinaryTree


def perform_move(tree):
    """
    get input
    """
    while True:
        try:
            num = int(input('Enter your move (1-9):'))
            if 0 <= num - 1 < 9:
                tree.move(num - 1)
                break
            else:
                print('Input should be between 1 and 9')
        except ValueError as error:
            print(error)


def play():
    tree = BinaryTree()

    print('Please choose who starts:\n')
    print('x - you start')
    print('o - bot starts')
    player = input()
    while player not in ["o", 'x']:
        player = input("Wrong input")
    print('\nBoard indices: \n-----\n|123|\n|456|\n|789|\n-----\n')

    if player == 'o':
        print(tree.board)
        tree.get_move()

    while not tree.winner:
        print(tree.board)
        perform_move(tree)
        if not tree.winner:
            print(tree.board)
            tree.get_move()

    print(tree.board)
    print('Winner: ', tree.winner)


if __name__ == '__main__':
    play()
