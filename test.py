# a = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         print(a[0][j])
#     print()


#
# print('11111111111111111')
# cl = "\n" * 100
# print(cl)

print('все ли размещено корректно, введите y/n') #проверка на правильность размещения, если не верно, то полный сброс
answer = ''
while answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N':
    answer = input()
    if answer == 'y' or answer == 'Y':
        ready = True
    elif answer == 'n' or answer == 'N':
        print(answer)
        # self.field = [['_'] * self.size for i in range(self.size)]
        # self.ship1coord = ({'sh1': []})
        # self.ship2coord = ({'sh2': []})
        # self.ship3coord = ({'sh3': []})
    else:
        print('введите правильный ответ: (y/n)')

