from game_board import GameBoard
import os
class PlayerMove:
    def __init__(self):
        self.game_board = GameBoard()
        self.positions = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        self.wrong_symbol = False

    def add_symbol(self, player, field):
        os.system('cls')
        symbol: str = ''
        if player == 1:
            symbol = 'X'
        else:
            symbol = 'O'

        if field == 'A1' and self.game_board.fields[0][0] == ' ':
            self.game_board.fields[0][0] = symbol
        elif field == 'A2' and self.game_board.fields[1][0] == ' ':
            self.game_board.fields[1][0] = symbol
        elif field == 'A3' and self.game_board.fields[2][0] == ' ':
            self.game_board.fields[2][0] = symbol
        elif field == 'B1' and self.game_board.fields[0][1] == ' ':
            self.game_board.fields[0][1] = symbol
        elif field == 'B2' and self.game_board.fields[1][1] == ' ':
            self.game_board.fields[1][1] = symbol
        elif field == 'B3' and self.game_board.fields[2][1] == ' ':
            self.game_board.fields[2][1] = symbol
        elif field == 'C1' and self.game_board.fields[0][2] == ' ':
            self.game_board.fields[0][2] = symbol
        elif field == 'C2' and self.game_board.fields[1][2] == ' ':
            self.game_board.fields[1][2] = symbol
        elif field == 'C3' and self.game_board.fields[2][2] == ' ':
            self.game_board.fields[2][2] = symbol
        else:
            self.wrong_symbol = True
            print('Wrong symbol')

        if field in self.positions:
            if not self.wrong_symbol:
                self.game_board.draw_board()