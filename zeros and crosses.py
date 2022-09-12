M = [['-', '-', '-'], # Список для отображения игровой доски и для реализации игровой логики
     ['-', '-', '-'],
     ['-', '-', '-']]

def playfield_printing():
    """Функция выводит игровую доску на экран"""
    print("  0 1 2")
    print("0 %s %s %s" % (tuple(M[0])))
    print("1 %s %s %s" % (tuple(M[1])))
    print("2 %s %s %s" % (tuple(M[2])))

def win_test(el, x, y):
    """Функция проверяет победил ли однин из игроков
    На вход получает el(это строка 'x' или 'o'), x и y - координаты"""
    number_of_elements = len([item for item in M[y] if item == el])
    # считаем количество повторных el(элементов 'x' или 'о')
    # по горизонтали с текущей координатой
    if number_of_elements == 3:
        print(f'Партия закончена, победили {el}')
        return 0
    number_of_elements = len([M[i][x] for i in range(3) if M[i][x] == el])
    # считаем количество повторных el(элементов 'x' или 'о')
    # по вертикали с текущей координатой

    if number_of_elements == 3:
        print(f'Партия закончена, победили {el}')
        return 0

    number_of_elements = len([M[i][i] for i in range(3) if M[i][i] == el])
    # считаем количество повторных el(элементов 'x' или 'о')
    # по диагонали которая идёт слева на право вниз
    if number_of_elements == 3:
        print(f'Партия закончена, победили {el}')
        return 0

    elem = [i for i in range(2, -1, -1)]
    # создаём список [2, 1, 0] для второй координаты при вызове списка М
    number_of_elements = len([M[i][elem[i]] for i in range(3) if M[i][elem[i]] == el])
    # считаем количество повторных el(элементов 'x' или 'о')
    # по диагонали которая идёт слева на право вверх
    if number_of_elements == 3:
        print(f'Партия закончена, победили {el}')
        return 0
    return 1

def cross():
    """Функция получает координаты крестика от пользователя и добавляет их в необходимый список
    и делае необходимые проверки печатает новую доску"""
    while True:
        coordinate_x = input("Введите координаты для x")
        x, y = tuple(map(int, coordinate_x.split()))
        if M[y][x] == '-':
            M[y][x] = "x"
            playfield_printing()
            if win_test('x', x, y) == 0:
                return 0
            break
        else:
            print("Ячейка занята")
    zerro()

def zerro():
    """Функция получает координаты нолика от пользователя и добавляет их в необходимый список
        и делае необходимые проверки печатает новую доску"""
    while True:
        coordinate_o = input("Введите координаты для o")
        x, y = tuple(map(int, coordinate_o.split()))
        if M[y][x] == '-':
            M[y][x] = "o"
            playfield_printing()
            if win_test('o', x, y) == 0:
                return 0
            break
        else:
            print("Ячейка занята")
    cross()
print('Игра крестики нолики')
print('Примечание: координаты вводите двумя числами через пробел,')
print('первая координата по горизонтали, вторая по вертикали')
playfield_printing()
cross()




