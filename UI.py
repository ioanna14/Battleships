class UserInterface:
    @staticmethod
    def input_move():
        line = input('Line: ')
        col = input('Column: ')
        direction = input('Direction: ')
        return line, col, direction

    @staticmethod
    def read_command():
        cmd = input('>')
        return cmd

    @staticmethod
    def read_move():
        line = input('Line (1-8): ')
        col = input('Column (A-H): ')
        return line, col

    @staticmethod
    def print_table(table):
        print('  A B C D E F G H ')
        for i in range(8):
            line = str(i + 1)
            for j in range(8):
                line += ' ' + table[i][j]
            print(line)

    @staticmethod
    def print_main_menu():
        print('1. Start.')
        print('2. Exit.')

    @staticmethod
    def print_ships_menu(which):
        if which == 0:
            print('Input Battleship coordinates (line, column, direction) beware the length is 4!')
        if which == 1:
            print('Input Cruiser coordinates (line, column, direction) beware the length is 3!')
        if which == 2:
            print('Input Destroyer coordinates (line, column, direction) beware the length is 2!')

    @staticmethod
    def congratulate(player):
        print('CONGRATULATIONS, player ' + str(player) + ' you won!!')

    @staticmethod
    def player1():
        print('Player 1: ')

    @staticmethod
    def player2():
        print('Player 2: ')
