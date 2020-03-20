class Board:
    def __init__(self):
        self.field = [['_','_','_']]

    def printField(self):
        for i in self.field:
            print()

f = Board()
for i in f.field:
    print(f.field)
