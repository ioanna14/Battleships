from UI import UserInterface
from Service import Service


class Application:
    def __init__(self, UI, service):
        self._UI = UI
        self._Service = service

    def start(self):
        """
        The start menu.
        :return: exit the game if the choice is 2.
        """
        while True:
            self._UI.print_main_menu()
            try:
                command = self._UI.read_command()
                if command == '1':
                    self.create_table()
                    self.start_game()
                elif command == '2':
                    return
                else:
                    raise ValueError('Bad command!')
            except ValueError as exception:
                print(exception.args[0])

    def create_table(self):
        """
        Creates 2 tables 1 table has random inputs and the other one has them from the console.
        :return: none
        """
        self._Service.init_table()
        counter = 0
        while counter != 3:
            self._UI.print_ships_menu(counter)
            line, col, direction = self._UI.input_move()
            try:
                line, col, direction, length = self._Service.validate_params(line, col, direction, 4 - counter)
                if self._Service.is_good_ship(line, col, direction, length, 1):
                    self._Service.ships_player1(line, col, direction, length)
                    counter += 1
            except ValueError as exception:
                print(exception.args[0])
            self._UI.print_table(self._Service.player1_table)
        self._UI.print_table(self._Service.player1_table)
        counter = 0
        while counter != 3:
            self._UI.print_ships_menu(counter)
            line, col, direction = self._Service.computer_params()
            try:
                line, col, direction, length = self._Service.validate_params(line, col, direction, 4 - counter)
                if self._Service.is_good_ship(line, col, direction, length, 2):
                    self._Service.ships_player2(line, col, direction, length)
                    counter += 1
            except ValueError as exception:
                print(exception.args[0])
            self._UI.print_table(self._Service.player2_table)
        self._UI.print_table(self._Service.player2_table)

    def start_game(self):
        """
        Starting the attack game, the player 1 inputs some position where
        he wants to attack, meanwhile the computer has a strategy if playing.
        :return: none
        """
        self._UI.print_table(self._Service.player1_table)
        while True:
            self.first_player_move()
            self._Service.check_sunk(2)
            if self._Service.check_win(1):
                self._UI.congratulate(1)
                break
            self.second_player_move()
            self._Service.check_sunk(1)
            if self._Service.check_win(2):
                self._UI.congratulate(2)
                break

    def first_player_move(self):
        """
        First player move.
        :return: none
        """
        self._UI.player1()
        attack = self._Service.player1_attack_table
        self._UI.print_table(attack)
        lin, col = self._UI.read_move()
        try:
            line, column = self._Service.validate_move(lin, col)
            self._Service.good_move(line, column, 1)
        except ValueError as exception:
            print(exception.args[0])
            self.first_player_move()
            return

    def second_player_move(self):
        """
        Second player, computer move.
        :return: none
        """
        self._UI.player2()
        attack = self._Service.player2_attack_table
        self._UI.print_table(attack)
        lin, col = self._Service.computer_strategy()
        try:
            self._Service.good_move(lin, col, 2)
        except IndexError:
            self.second_player_move()
            return
        except ValueError as exception:
            print(exception.args[0])
            self.second_player_move()
            return


ui = UserInterface()
Service = Service()
application = Application(ui, Service)
application.start()
