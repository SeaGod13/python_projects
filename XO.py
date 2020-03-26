class Board:
    def __init__(self):
        self.field = [['_','_','_']] * 3

    def printField(self):
        print('  0', '1', '2')
        for i in range(3):
            print(i, end=' ')
            for j in range(3):
                print(self.field[i][j], end = ' ')
            print()
arg = Board()
arg.printField()
print()
arg.field[1][0] = 'X'
arg.printField()

