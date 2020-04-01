class Board:
    def __init__(self):
        self.size = 3
        self.field = [['_'] * self.size for i in range(self.size)]

    def printField(self):
        print('  ', end='')
        for i in range(self.size):
            print(i, end=' ')
        print()
        for i in range(self.size):
            print(i, end=' ')
            for j in range(self.size):
                print(self.field[i][j], end=' ')
            print()

    def win_check(self, player):
        # первая проверка диагональ 00 -- 22
        flag = False
        cnt = 0
        while cnt == 0:
            for i in range(self.size-1):
                if arg.field[i][i] == arg.field[i+1][i+1]:
                    flag = True
                    cnt += 1
            if cnt == self.size - 1 and flag:
                cnt = 1
                return flag
            break
        # вторая проверка диагональ 02 -- 20
        flag = False
        cnt = 0
        while cnt == 0:
            for i in range(self.size - 1):
                if arg.field[i][self.size - 1 - i] == arg.field[i + 1][self.size - 1 - i - 1]:
                    flag = True
                    cnt += 1
            if cnt == self.size - 1 and flag:
                cnt = 1
                return flag
            break
        # третья проверка горизонтали
        for i in range(self.size):
            flag = False
            cnt = 0
            for j in range(self.size - 1):
                # a = arg.field[i][j]
                # b = arg.field[i][j+1]
                if arg.field[i][j] == arg.field[i][j+1] != '_':
                    flag = True
                    cnt += 1
            if cnt == self.size - 1 and flag:
                return flag
        # червертая проверка вертикали
        for j in range(self.size):
            flag = False
            cnt = 0
            for i in range(self.size - 1):
                # a = arg.field[i][j]
                # b = arg.field[i+1][j]
                if arg.field[i][j] == arg.field[i+1][j] != '_':
                    flag = True
                    cnt += 1
            if cnt == self.size - 1 and flag:
                return flag

arg = Board()
arg.printField()
print()
winner = False
lblx = 'X'
lblo = 'O'
count = 0
while not winner and count < 10:
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
    if count > 4:
        winner = arg.win_check(lbl)
    if lbl == 'X' and winner:
        print('Победа крестиков')
    elif lbl == 'O' and winner:
        print('Победа ноликов')


