import time

class Map:
    def __init__(self):
        self.size = 6  # размер поля
        self.field = [['_'] * self.size for i in range(self.size)]
        self.ship1cnt = 3  # кол-во 1 палубных кораблей
        self.ship2cnt = 2  # кол-во 2 палубных кораблей
        self.ship3cnt = 1  # кол-во 3 палубных кораблей

    # метод печати поля
    def printField(self):
        print('  0', '1', '2', '3', '4', '5')
        for i in range(self.size):
            print(i, end=' ')
            for j in range(self.size):
                print(self.field[i][j], end=' ')
            print()
        print()

    # метод заполнения поля
    def fillField(self):
        ready = False
        while not ready:
            # расстановка однопалубных кораблей
            cnt = 0
            print('расставьте три 1 палубных корабля')
            while cnt < self.ship1cnt:
                cnt += 1
                print('введите координаты корабля №' + str(cnt))
                x = int(input())
                y = int(input())
                while x >= self.size or y >= self.size or self.field[y][x] == 'O':
                    print('введите правильные координаты')
                    x = int(input())
                    y = int(input())
                self.field[y][x] = 'O'
            self.printField()
            # расстановка двухпалубных кораблей
            cnt = 0
            n = self.ship2cnt
            print('расставьте два 2 палубных корабля')
            while cnt < n:
                cnt += 1
                print('введите начальные координаты корабля №' + str(cnt))
                x = int(input())
                y = int(input())
                while x >= self.size or y >= self.size or self.field[y][x] == 'O':
                    print('введите правильные координаты')
                    x = int(input())
                    y = int(input())
                self.field[y][x] = 'O'
                print('введите смещение в ' + str(n-1) + ' кл. по любой из коодинат для корабля №' + str(cnt))
                delta_x = int(input())
                delta_y = int(input())
                while x + delta_x >= self.size or y + delta_y >= self.size or self.field[y + delta_y][x + delta_x] == 'O' \
                        or delta_x < -(n-1) or delta_y < -(n-1) or delta_x > (n-1) or delta_y > (n-1) \
                        or (delta_x != 0 and delta_y != 0):
                    print('введите правильное смещение')
                    delta_x = int(input())
                    delta_y = int(input())
                self.field[y + delta_y][x + delta_x] = 'O'
            self.printField()
            # расстановка трехпалубных кораблей
            cnt = 0
            n = self.ship3cnt
            print('расставьте один 3 палубный корабль')
            while cnt < n:
                cnt += 1
                print('введите начальные координаты корабля №' + str(cnt))
                x = int(input())
                y = int(input())
                while x >= self.size or y >= self.size or self.field[y][x] == 'O':
                    print('введите правильные координаты')
                    x = int(input())
                    y = int(input())
                self.field[y][x] = 'O'
                print('введите смещение в ' + str(n+1) + ' кл. по любой из коодинат для корабля №' + str(cnt))
                delta_x = int(input())
                delta_y = int(input())
                while x + delta_x >= self.size or y + delta_y >= self.size or self.field[y + delta_y][x + delta_x] == 'O' \
                        or delta_x < -(n+1) or delta_y < -(n+1) or delta_x > (n+1) or delta_y > (n+1) \
                        or (delta_x != 0 and delta_y != 0):
                    print('введите правильное смещение')
                    delta_x = int(input())
                    delta_y = int(input())
                if delta_x == 0 and delta_y != 0:
                    self.field[y + delta_y - 1][x + delta_x] = 'O'
                elif delta_x != 0 and delta_y == 0:
                    self.field[y + delta_y][x + delta_x - 1] = 'O'
                self.field[y + delta_y][x + delta_x] = 'O'
            self.printField()
            print('все ли размещено корректно, введите y/n')
            answer = input()
            if answer == 'y' or answer == 'Y':
                ready = True
        return self.field

    # метод определения победителя
    def winCheck(self):
        winCnt = 0
        win = False
        for i in range(self.size):
            for j in range(self.size):
                if self.field[y][x] == '*':
                    winCnt += 1
        if winCnt == 10:
            win = True
        return win

cls = "\n" * 20  # переменная для очистки поля

# инициализация полей
p1_ob = Map()
p1_fb = Map()
p2_ob = Map()
p2_fb = Map()

# заполнение полей первым игроком
p1_ob.printField()
p1_fb.printField()
print()
print('первый игрок')
p1_ob.fillField()
p1_ob.printField()
p1_fb.printField()
time.sleep(3)
print(cls)

# заполнение полей вторым игроком
p2_ob.printField()
p2_fb.printField()
print()
print('второй игрок')
p2_ob.fillField()
p2_ob.printField()
p2_fb.printField()
time.sleep(3)
print(cls)

# активная фаза игры
trn = 0
trnCnt = 0
finish = False
while not finish:
    trn += 1
    trnCnt += 1
    miss = False
    if trn % 2 != 0:
        p1_ob.printField()
        p1_fb.printField()
        while not miss:
            print('первый игрок введите координаты стрельбы')
            x = int(input())
            y = int(input())
            if p2_ob.field[y][x] == '.':
                print('вы стреляли по этому полю, еще раз введите координаты стрельбы')
                x = int(input())
                y = int(input())
            elif p2_ob.field[y][x] == '_':
                p2_ob.field[y][x] = '.'
                p1_fb.field[y][x] = '.'
                print('вы промахнулись')
                miss = True
            elif p2_ob.field[y][x] == 'O':
                p2_ob.field[y][x] = '*'
                p1_fb.field[y][x] = '*'
                if p2_ob.field[y+1][x] == 'O' or p2_ob.field[y-1][x] == 'O' or p2_ob.field[y][x+1] == 'O' \
                        or p2_ob.field[y][x] == 'O':
                    print('ранил, стреляйте дальше')
                else:
                    print('убили, ищите новую цель')
                trnCnt += 1
            p1_ob.printField()
            p1_fb.printField()
        if trnCnt > 9:
            finish = p2_ob.winCheck()
    else:
        p2_ob.printField()
        p2_fb.printField()
        while not miss:
            print('второй игрок введите координаты стрельбы')
            x = int(input())
            y = int(input())
            if p1_ob.field[y][x] == '.':
                print('вы стреляли по этому полю, еще раз введите координаты стрельбы')
                x = int(input())
                y = int(input())
            elif p1_ob.field[y][x] == '_':
                p1_ob.field[y][x] = '.'
                p2_fb.field[y][x] = '.'
                print('вы промахнулись')
                miss = True
            elif p1_ob.field[y][x] == 'O':
                p1_ob.field[y][x] = '*'
                p2_fb.field[y][x] = '*'
                if p1_ob.field[y + 1][x] == 'O' or p1_ob.field[y - 1][x] == 'O' or p1_ob.field[y][x + 1] == 'O' \
                        or p1_ob.field[y][x] == 'O':
                    print('ранил, стреляйте дальше')
                else:
                    print('убили, ищите новую цель')
                trnCnt += 1
            p2_ob.printField()
            p2_fb.printField()
        if trnCnt > 9:
            finish = p1_ob.winCheck()
    time.sleep(3)
    print(cls)
if trn % 2 != 0:
    print('победа первого игрока')
else:
    print('победа второго игрока')
