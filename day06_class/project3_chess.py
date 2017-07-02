class Unit(object):
    def __init__(self, name, side, position, board):
        self.name = name
        self.side = side
        self.position = position
        self.board = board

    def available_path(self):
        pass

    def move(self, x, y):
        pass

    def check_path(self, x, y):
        if all(0 <= p < 8 for p in (x, y)):
            if self.board[x][y] == None:
                return True
            elif self.board[x][y].side != self.side:
                return True

        return False

    def __str__(self):
        return '{}{}'.format(self.name, self.side)

    def __repr__(self):
        return '{}{}'.format(self.name, self.side)

class Pawn(Unit):
    def __init__(self, side, position, board):
        super(Pawn, self).__init__('P', side, position, board)

    def available_path(self):
        paths = []

        direction = 1
        if self.side == 1:
            direction = -1

        for dx, dy in ((direction, 0), (0, 1), (0, -1)):
            x, y = self.position
            if self.check_path(x+dx, y+dy)
                paths.append((x+dx, y+dy))

    def move(self, x, y):
        pass

class Look(Unit):
    def __init__(self, side, board):
        super(Pawn, self).__init__('L', side, board)

    def available_path(self):


    def move(self, x, y):
        pass



class ChessBoard(object):
    def __init__(self):
        self.board = [[None] * 8 for i in range(8)]

    def show_board(self):
        pass
