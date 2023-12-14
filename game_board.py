class GameBoard:
    fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def draw_board(self):
        i = 0
        print('   A   B   C  ')
        for index,f in enumerate(self.fields):
            print(f'{index+1}  {f[i]} | {f[i+1]} | {f[i+2]} ')

    def check_if_player_x_win(self) -> bool:
        if self.fields[0][0] == 'X' and self.fields[0][1] == 'X' and self.fields[0][2] == 'X':
            return True
        elif self.fields[1][0] == 'X' and self.fields[1][1] == 'X' and self.fields[1][2] == 'X':
            return True
        elif self.fields[2][0] == 'X' and self.fields[2][1] == 'X' and self.fields[2][2] == 'X':
            return True
        elif self.fields[0][0] == 'X' and self.fields[1][0] == 'X' and self.fields[2][0] == 'X':
            return True
        elif self.fields[0][1] == 'X' and self.fields[1][1] == 'X' and self.fields[2][2] == 'X':
            return True
        elif self.fields[0][2] == 'X' and self.fields[1][2] == 'X' and self.fields[2][2] == 'X':
            return True
        elif self.fields[0][0] == 'X' and self.fields[1][1] == 'X' and self.fields[2][2] == 'X':
            return True
        elif self.fields[0][2] == 'X' and self.fields[1][1] == 'X' and self.fields[2][0] == 'X':
            return True
        else:
            return False

    def check_if_player_o_win(self) -> bool:
        if self.fields[0][0] == 'O' and self.fields[0][1] == 'O' and self.fields[0][2] == 'O':
            return True
        elif self.fields[1][0] == 'O' and self.fields[1][1] == 'O' and self.fields[1][2] == 'O':
            return True
        elif self.fields[2][0] == 'O' and self.fields[2][1] == 'O' and self.fields[2][2] == 'O':
            return True
        elif self.fields[0][0] == 'O' and self.fields[1][0] == 'O' and self.fields[2][0] == 'O':
            return True
        elif self.fields[0][1] == 'O' and self.fields[1][1] == 'O' and self.fields[2][2] == 'O':
            return True
        elif self.fields[0][2] == 'O' and self.fields[1][2] == 'O' and self.fields[2][2] == 'O':
            return True
        elif self.fields[0][0] == 'O' and self.fields[1][1] == 'O' and self.fields[2][2] == 'O':
            return True
        elif self.fields[0][2] == 'O' and self.fields[1][1] == 'O' and self.fields[2][0] == 'O':
            return True
        else:
            return False