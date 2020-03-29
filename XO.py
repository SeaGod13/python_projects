class Board:
    def __init__(self):
        self.size = 3
        self.field = [['_'] * self.size for i in range(self.size)]

    def printField(self):
        print('  0', '1', '2')
        for i in range(3):
            print(i, end=' ')
            for j in range(3):
                print(self.field[i][j], end = ' ')
            print()

    def win_check(self, player):
        i = 0
        game_over == False
        win_count = 0
        while i < self.size - 1:
            if arg.field[i][i] == arg.field[i+1][i+1]: # 00-22
                win_count += 1
            if win_count == self.size - 1:
                game_over = True
            i += 1
        if player == 'X' and game_over == True:
            win_X = True
        elif player == 'O' and game_over == True:
            win_O = True




        # if (arg.field[0][0] == arg.field[1][1] and arg.field[1][1] == arg.field[2][2]): # 00 - 22
        #     game_over = True
        # elif (arg.field[0][0] == arg.field[0][1] and arg.field[0][1] == arg.field[0][2]): # 00 - 02
        #     game_over = True
        # elif (arg.field[0][0] == arg.field[1][0] and arg.field[1][0] == arg.field[2][0]): #
        #     game_over = True
        # elif (arg.field[0][2] == arg.field[1][1] and arg.field[1][1] == arg.field[2][0]):
        #     game_over = True


arg = Board()
arg.printField()
print()
win_X = False
win_O = False
lblx = 'X'
lblo = 'O'
count = 0
while win_X == False and win_O == False and count < 10:
    count += 1

    if count % 2 != 0:
        move = 'Крестики, '
        lbl = lblx
    else:
        move = 'Нолики, '
        lbl = lblo
    print(move + 'введите координаты')
    print('по горизонтали')
    x = int(input())
    if x < 0 or x > arg.size - 1:
        print('введите правильные координаты по горизонтали')
    print('по вертикали')
    y = int(input())
    if y < 0 or y > arg.size - 1:
        print('введите правильные координаты по вертикали')
    if arg.field[y][x] != '_':
        print('!!! введите правильные координаты !!!')
        print()
        count -= 1
    else:
        arg.field[y][x] = lbl
    arg.printField()
    print()
    if count > 0:
        arg.win_check(lbl)
    if win_X:
        print('Победа крестиков')
    elif win_O:
        print('Победа ноликов')
        # if (arg.field[0][0] == arg.field[1][1] and arg.field[1][1] == arg.field[2][2]):
        #     if arg.field[0][0] == lblx:
        #         print('Победа крестиков')
        #         win_X = True
        #     elif arg.field[0][0] == lblo:
        #         print('Победа ноликов')
        #         win_O = True


