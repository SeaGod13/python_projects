class Board:
    def __init__(self):
        #self.field = [['_','_','_']]
        self.size = 3
        self.field = [['_'] * self.size for i in range(self.size)]

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
win_X = 0
win_O = 0
count = 0
while win_X == 0 or win_O == 0 or count < 10:
    win_X = 1
    count += 1
    lblx = 'X'
    lblo = 'O'
    if count % 2 != 0:
        move = 'Крестики, '
        lbl = lblx
    else:
        move = 'Нолики, '
        lbl = lblo
    print(move + 'введите координаты')
    print('по горизонтали')
    x = int(input())
    if x < 0 or x > 2:
        print('введите правильные координаты по горизонтали')
    print('по вертикали')
    y = int(input())
    if y < 0 or y > 2:
        print('введите правильные координаты по вертикали')
    if arg.field[y][x] != '_':
        print('!!! введите правильные координаты !!!')
        print()
        count -= 1
    else:
        arg.field[y][x] = lbl
    arg.printField()
    print()
    if count > 4:
        if (arg.field[0][0] == arg.field[1][1] and arg.field[1][1] == arg.field[2][2]):
            if arg.field[0][0] == lblx:
                print('Победа крестиков')
                win_X = 1
            elif arg.field[0][0] == lblo:
                print('Победа ноликов')
                win_O = 1


