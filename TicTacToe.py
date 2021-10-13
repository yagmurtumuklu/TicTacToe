import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def __init__(self, board):
        self.board = []
        print('   |   |')
        print(' ' + board[1] + ' || ' + board[2] + ' || ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' || ' + board[5] + ' || ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' || ' + board[8] + ' || ' + board[9])
        print('   |   |')

    def get_player_1(self):
        return random.randint(0,1)

    def square_change (self, row, column, player):
        self.board[row][column] = player

    def player_win(self, player):
        win = None

        n = len(self.board)

########checkkkkkkk
    #row kontrol
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

    # column kontrol
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

    # köşegen kontrol

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
                if win:
                    return win

                win = True
                for i in range(n):
                    if self.board[i][n - 1 - i] != player:
                        win = False
                        break
                if win:
                    return win
                return False

                for row in self.board:
                    for item in row:
                        if item == '-':
                            return False
                return True

            def board_full(self):
                for row in self.board:
                    for item in row:
                        if item == '-':
                            return False

                return True

            def player_turn(self, player):
                return 'X' if iplayer == '0' else '0'

            def board_show(self):
                for row in self.board:
                    for item in row:
                        print(item, end = '-')

                    pirnt()

            def start(self):
                self.create_board()

                player = 'X' if self.get_random_first_player() == 1 else 'O'
                while True:
                    print(f"{player}:")
                    self.show_board()

                    row, col = list(
                        map(int, input("Enter row and column numbers: ").split()))
                    print()

                    self.fix_spot(row - 1, col - 1, player)

                    # checking win
                    if self.is_player_win(player):
                        print(f"Player {player} wins!")
                        break

                    # checking beraberlik
                    if self.is_board_filled():
                        print("Draw!")
                        break

                    #
                    player = self.swap_player_turn(player)

            # final board
                print()
                self.show_board()


            tic_tac_toe = TicTacToe()
            tic_tac_toe.start()



