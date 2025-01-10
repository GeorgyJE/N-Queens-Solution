'''this is the basic class that the interactive board uses in order to keep track of all the attacked squares
and the squares that have a queen on them.'''
class X:
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.queens = 0
        self.IsQueen = False
        self.queens = 0
        self.color = ""

