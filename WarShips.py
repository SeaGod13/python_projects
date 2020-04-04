class Map:
    def __init__(self):
        self.size = 6        # размер поля
        self.field = [['_'] * self.size for i in range(self.size)]
        self.ship1cnt = 3    # кол-во 1 палубных кораблей
        self.ship2cnt = 2    # кол-во 2 палубных кораблей
        self.ship3cnt = 1    # кол-во 3 палубных кораблей

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
            print('расставьте два 2 палубных корабля')
            while cnt < self.ship2cnt:
                cnt += 1
                print('введите начальные координаты корабля №' + str(cnt))
                x = int(input())
                y = int(input())
                while x >= self.size or y >= self.size or self.field[y][x] == 'O':
                    print('введите правильные координаты')
                    x = int(input())
                    y = int(input())
                self.field[y][x] = 'O'
                print('введите смещение в 1 клетку по любой из коодинат для корабля №' + str(cnt))
                delta_x = int(input())
                delta_y = int(input())
                while x + delta_x >= self.size or y + delta_y >= self.size or self.field[y + delta_y][x + delta_x] == 'O' \
                        or  delta_x < -1 or  delta_y < -1 or  delta_x > 1 or  delta_y > 1 or (delta_x != 0 and delta_y != 0):
                    print('введите правильное смещение')
                    delta_x = int(input())
                    delta_y = int(input())
                self.field[y + delta_y][x + delta_x] = 'O'
            self.printField()
            # расстановка трехпалубных кораблей
            cnt = 0
            while cnt < self.ship3cnt:
                cnt += 1
                print('введите начальные координаты корабля №' + str(cnt))
                x = int(input())
                y = int(input())
                while x >= self.size or y >= self.size or self.field[y][x] == 'O':
                    print('введите правильные координаты')
                    x = int(input())
                    y = int(input())
                self.field[y][x] = 'O'
                print('введите смещение в 2 клетки по любой из коодинат для корабля №' + str(cnt))
                delta_x = int(input())
                delta_y = int(input())
                while x + delta_x >= self.size or y + delta_y >= self.size or self.field[y + delta_y][x + delta_x] == 'O' \
                        or  delta_x < -2 or  delta_y < -2 or  delta_x > 2 or  delta_y > 2 or (delta_x != 0 and delta_y != 0):
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
            
cls = "\n" * 20  # переменная для очистки поля

# while not winner:
#     winner = True
p1_ob = Map()
p1_fb = Map()
p2_ob = Map()
p2_fb = Map()

p1_ob.printField()
p1_fb.printField()
print()

p1_ob.fillField()
p1_ob.printField()
# print(cls)
