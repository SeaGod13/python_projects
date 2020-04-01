class Map:
    def __init__(self):
        self.size = 6
        self.field = [['_'] * self.size for i in range(self.size)]

    def printField(self):
        print('  0', '1', '2', '3', '4', '5', '   ', '0', '1', '2', '3', '4', '5')
        for i in range(6):
            print(i, end=' ')
            for j in range(6):
                print(self.field[i][j], end=' ')
            print()

# while not winner:
#     winner = True
arg = Map()
arg.printField()
print()