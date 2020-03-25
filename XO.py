class Board:
    def __init__(self):
        self.field = [['_','_','_']] * 3

    def printField(self):
        f = Board()
        print('    0 ', '  1 ', '  2')
        for i in range(3):
            print(str(i), end=' ')
            print(f.field[i])

arg = Board()
arg.printField()


