import random


class Service:
    def __init__(self):
        self._player1 = []
        self._player2 = []
        self._attack_player1 = []
        self._attack_player2 = []

    @property
    def player1_table(self):
        return self._player1

    @property
    def player1_attack_table(self):
        return self._attack_player1

    @property
    def player2_table(self):
        return self._player2

    @property
    def player2_attack_table(self):
        return self._attack_player2

    def init_table(self):
        for i in range(8):
            star = []
            for j in range(8):
                star.append('*')
            self._player1.append(star[:])
            self._player2.append(star[:])
            self._attack_player1.append(star[:])
            self._attack_player2.append(star[:])

    @staticmethod
    def validate_params(lin, col, direction, length):
        """
        Validate the params for the ships.
        :param lin: the line where we start to have a ship
        :param col: the column where we start to have a ship
        :param direction: the direction in which the ship will be placed
        :param length: the length of the ship
        :return: line, column, direction, length
        """
        if not lin.isdigit() or 8 < int(lin) < 0:
            raise ValueError('Bad input!')
        line = int(lin) - 1
        translator = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
        }
        if not col.isalpha():
            raise ValueError('The column must be between A and H!')
        col = col.upper()
        if col not in translator:
            raise ValueError('The column must be between A and H!')
        column = translator[col] - 1
        if direction not in ['right', 'down']:
            raise ValueError('The direction must be down or right!')
        return line, column, direction, length

    def is_good_ship(self, line, col, direction, length, player):
        """
        Check dor each player if the place where they put the ship is valid.
        :param line: the line where we start to have a ship
        :param col: the column where we start to have a ship
        :param direction: the direction in which the ship will be placed
        :param length: the length of the ship
        :param player: the player 1 or the computer, which is player 2
        :return: true if it's valid
        """
        if player == 1:
            for i in range(length):
                if direction == 'right':
                    if col + i > 7:
                        raise ValueError('Bad coordinates!')
                    if self._player1[line][col + i] != '*':
                        raise ValueError('Bad coordinates!')
                if direction == 'down':
                    if line + i > 7:
                        raise ValueError('Bad coordinates!')
                    if self._player1[line + i][col] != '*':
                        raise ValueError('Bad coordinates!')
            return True
        if player == 2:
            for i in range(length):
                if direction == 'right':
                    if col + i > 7:
                        raise ValueError('Bad coordinates!')
                    if self._player2[line][col + i] != '*':
                        raise ValueError('Bad coordinates!')
                if direction == 'down':
                    if line + i > 7:
                        raise ValueError('Bad coordinates!')
                    if self._player2[line + i][col] != '*':
                        raise ValueError('Bad coordinates!')
            return True

    def ships_player1(self, line, col, direction, length):
        """
        Puts 'B' where we have the battleship, 'C' where we have the
        cruiser and 'D' where we have the destroyer.
        :param line: the line where we start to have a ship
        :param col: the column where we start to have a ship
        :param direction: the direction in which the ship will be placed
        :param length: the length of the ship
        :return: none
        """
        ships_map = {
            4: 'B',
            3: 'C',
            2: 'D',
        }
        for i in range(length):
            if direction == 'right':
                self._player1[line][col + i] = ships_map[length]
            elif direction == 'down':
                self._player1[line + i][col] = ships_map[length]

    def ships_player2(self, line, col, direction, length):
        """
        Puts 'B' where we have the battleship, 'C' where we have the
        cruiser and 'D' where we have the destroyer.
        :param line: the line where we start to have a ship
        :param col: the column where we start to have a ship
        :param direction: the direction in which the ship will be placed
        :param length: the length of the ship
        :return: none
        """
        ships_map = {
            4: 'B',
            3: 'C',
            2: 'D',
        }
        for i in range(length):
            if direction == 'right':
                self._player2[line][col + i] = ships_map[length]
            elif direction == 'down':
                self._player2[line + i][col] = ships_map[length]

    def check_win(self, player):
        """
        Checks which player won, each time we have an attack.
        :param player: 1 or the computer
        :return: true if one of the players won
        """
        counter = 0
        if player == 1:
            for x in range(8):
                for y in range(8):
                    if self._attack_player1[x][y] != '*' and self._attack_player1[x][y] != 'O':
                        counter += 1
            if counter == 9:
                return True
        counter = 0
        if player == 2:
            for x in range(8):
                for y in range(8):
                    if self._attack_player2[x][y] != '*' and self._attack_player2[x][y] != 'O':
                        counter += 1
            if counter == 9:
                return True

    def check_sunk(self, player):
        """
        Check if one of the ships is sunk and tell the
        player which one is sunk, each attack.
        :param player: 1 or the computer
        :return: the letter corresponding to the ship that is sunk
        """
        b = 0
        c = 0
        d = 0
        if player == 1:
            for x in range(8):
                for y in range(8):
                    if self._player1[x][y] == 'b':
                        b += 1
                    if self._player1[x][y] == 'c':
                        c += 1
                    if self._player1[x][y] == 'd':
                        d += 1
            if b == 4:
                for x in range(8):
                    for y in range(8):
                        if self._player1[x][y] == 'b':
                            self._attack_player2[x][y] = 'B'
            if c == 3:
                for x in range(8):
                    for y in range(8):
                        if self._player1[x][y] == 'c':
                            self._attack_player2[x][y] = 'C'
            if d == 2:
                for x in range(8):
                    for y in range(8):
                        if self._player1[x][y] == 'd':
                            self._attack_player2[x][y] = 'D'
        b = 0
        c = 0
        d = 0
        if player == 2:
            for x in range(8):
                for y in range(8):
                    if self._player2[x][y] == 'b':
                        b += 1
                    if self._player2[x][y] == 'c':
                        c += 1
                    if self._player2[x][y] == 'd':
                        d += 1
            if b == 4:
                for x in range(8):
                    for y in range(8):
                        if self._player2[x][y] == 'b':
                            self._attack_player1[x][y] = 'B'
            elif c == 3:
                for x in range(8):
                    for y in range(8):
                        if self._player2[x][y] == 'c':
                            self._attack_player1[x][y] = 'C'
            elif d == 2:
                for x in range(8):
                    for y in range(8):
                        if self._player2[x][y] == 'd':
                            self._attack_player1[x][y] = 'D'

    @staticmethod
    def validate_move(lin, col):
        """
        Validate the move of each attack.
        :param lin: the line where we want to attack
        :param col: the column of the place where we want to attack
        :return: line and column
        """
        if not lin.isdigit() or 8 < int(lin) < 0:
            raise ValueError('Bad input!')
        line = int(lin) - 1
        translator = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
        }
        if not col.isalpha():
            raise ValueError('The column must be between A and H!')
        col = col.upper()
        if col not in translator:
            raise ValueError('The column must be between A and H!')
        column = translator[col] - 1
        return line, column

    def good_move(self, lin, col, player):
        """
        Checks if we attacked that place before and puts X
        if the move is good and O if the move is ot good.
        :param lin: line of the move
        :param col: column of the move
        :param player: 1 or the computer
        :return: none
        """
        players_map = {
            1: [self._attack_player1, self._player2],
            2: [self._attack_player2, self._player1],
        }
        attack_table = players_map[player][0]
        table = players_map[player][1]
        if attack_table[lin][col] != '*':
            raise ValueError('You already attacked this place!')
        else:
            if table[lin][col] != '*':
                attack_table[lin][col] = 'X'
                table[lin][col] = table[lin][col].lower()
            else:
                attack_table[lin][col] = 'O'
                table[lin][col] = 'O'

    @staticmethod
    def computer_params():
        """
        Choose the computer params for ships, randomly.
        :return: line, column, direction
        """
        lin = ['1', '2', '3', '4', '5', '6', '7', '8']
        col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        direction = ['right', 'down']
        line = random.choice(lin)
        column = random.choice(col)
        direct = random.choice(direction)
        return line, column, direct

    def computer_attack_random(self):
        lin = ['1', '2', '3', '4', '5', '6', '7', '8']
        col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        a = random.choice(lin)
        b = random.choice(col)
        line, column = self.validate_move(a, b)
        return line, column

    def computer_strategy(self):
        """
        Looks for a previous hit and computes a strategy or selects a random place
        if it doesn't find a previous hit.
        """
        for x in range(8):
            for y in range(8):
                if self._attack_player2[x][y] == 'X':
                    if self.neighbours(x, y):
                        line, col = self.neighbours(x, y)
                        return line, col
        return self.random_attack()

    def neighbours(self, x, y):
        """
        Finds the neighbours of an X and try to attack there.
        :param x: the line
        :param y: the column
        :return: line and column if it finds a neighbour and false if not
        """
        directions = {
            'up': [x - 2, y],
            'right': [x, y + 2],
            'down': [x + 2, y],
            'left': [x, y - 2],
            None: None
        }
        direction = self.nearest_x(x, y)
        if directions[direction] is None:
            line = self.random_around(x, y)[0]
            col = self.random_around(x, y)[1]
            return line, col
        line = directions[direction][0]
        col = directions[direction][1]
        if line in range(8) and col in range(8):
            if self._attack_player2[line][col] == "*":
                return line, col
        return False

    def nearest_x(self, x, y):
        """
        Finds the nearest X.
        :param x: line
        :param y: column
        :return: where is the next attack supposed to be or none if there is no X around
        """
        if x - 1 in range(8):
            if self._attack_player2[x - 1][y] == 'X':
                return 'up'
        if y + 1 in range(8):
            if self._attack_player2[x][y + 1] == 'X':
                return 'right'
        if x + 1 in range(8):
            if self._attack_player2[x + 1][y] == 'X':
                return 'down'
        if y - 1 in range(8):
            if self._attack_player2[x][y - 1] == 'X':
                return 'left'
        return None

    @staticmethod
    def random_attack():
        """
        Attacks random on the table.
        :return: line and column
        """
        indices = list(range(64))
        val = None
        for i in range(64):
            val = random.choice(indices)
            indices.remove(val)
        return val // 8, val % 8

    @staticmethod
    def random_around(x, y):
        """
        Attacks randomly around an X.
        :param x: line
        :param y: column
        :return: line and column
        """
        choices = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        return random.choice(choices)
