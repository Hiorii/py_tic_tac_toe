from player_move import PlayerMove
from game_board import GameBoard

if __name__ == '__main__':
    is_game = True
    game_board = GameBoard()
    game_board.draw_board()
    index = 1
    while is_game:
        player_move = PlayerMove()
        if index % 2 == 0:
            player1 = input('Player 1 move: \n')
            player_move.add_symbol(1, player1)
        else:
            player2 = input('Player 2 move: \n')
            player_move.add_symbol(2, player2)

        game_board.check_if_player_o_win()
        if not player_move.wrong_symbol:
            index += 1
        if game_board.check_if_player_x_win():
            print('Player 1 Win')
            is_game = False

        if game_board.check_if_player_o_win():
            print('Player 2 Win')
            is_game = False

