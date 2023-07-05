from typing import *


def setup():
    """
    Функция инициализации
    Ничего не возвращает.
    Выводит информацию об игре и рисует пустое поле
    """
    print('Добро пожаловать в игру "Крестики-нолики"\n')
    print('Кре́стики-но́лики — логическая игра между двумя противниками на квадратном поле 3 на 3 клетки.\n')
    print('Правила игры:')
    print("""Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). 
    Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает. 
    Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, 
    горизонтали или большой диагонали нет трёх одинаковых знаков, партия считается закончившейся в ничью. 
    Первый ход делает игрок, ставящий крестики.""")
    print('\nКоординаты можно вводить как слитно, так и через пробел, запятую или любой другой знак препинания\n')


def print_field(field):
    cell_sep = ' | '
    rows = len(field)
    cols = len(field[0])

    col_width = []
    for col in range(cols):
        columns = [field[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    for i, row in enumerate(range(rows)):
        if i == 1:
            print(separator)

        result = []
        for col in range(cols):
            item = field[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))


def init_field() -> tuple:
    """
    Инициализация игрового поля
    Возвращая tuple(Первый игрок, продолжать игру, игровая Таблица)
    :return: tuple
    """
    # Чтобы увеличить поле, достаточно расширить массив до нужных размеров
    field = [
        ['', '1', '2', '3'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-']
    ]
    # field = [
    #     ['', '1', '2', '3', '4'],
    #     ['1', '-', '-', '-', '-'],
    #     ['2', '-', '-', '-', '-'],
    #     ['3', '-', '-', '-', '-'],
    #     ['4', '-', '-', '-', '-'],
    # ]
    print_field(field)
    return True, True, field


def check_coord(coord: str, len_field: int) -> Optional[tuple]:
    """
    Проверяю корректность ввода координат
    :param coord: str
    :param len_field: int
    :return: tuple or None
    """
    # Проверяю что введены обе координаты корректно
    new_coord = tuple(int(i) for i in coord if i and i.isdigit() and 0 < int(i) < len_field)
    if len(new_coord) != 2:
        print('Вы ввели некорректно координаты. Повторите попытку')
        print('Необходимо ввести две цифры от 1 до 3')
        new_coord = None

    return None or new_coord


def check_field(field: list) -> int:
    """
    Проверяю все возможные варианты для выигрыша
    :param field:
    :return: int
    0 - продолжаем
    1 - 1 игрок выиграл
    2 - 2 игрок выиграл
    3 - ничья
    """
    win_x = 'X' * (len(field) - 1)
    win_y = 'O' * (len(field) - 1)
    for i in range(1, len(field[0])):
        check_x = [field[i][u] for u in range(1, len(field))]
        check_y = [field[u][i] for u in range(1, len(field))]
        str_x = ''.join(check_x)
        str_y = ''.join(check_y)
        if str_x == win_x or str_y == win_x:
            return 1
        elif str_x == win_y or str_y == win_y:
            return 2

    # Проверка диагоналей
    check_1 = [field[u][u] for u in range(1, len(field))]
    check_2 = [field[x][y] for x, y in zip(range(1, len(field)), range(len(field)-1, 0, -1))]
    str_1 = ''.join(check_1)
    str_2 = ''.join(check_2)
    if str_1 == win_x or str_2 == win_x:
        return 1
    elif str_1 == win_y or str_2 == win_y:
        return 2

    if '-' in [i for row in field for i in row]:
        return 0
    return 3


def loop(main_data: tuple) -> tuple:
    """
    Основная функция программы
    :return: bool
    """
    field = main_data[2].copy()
    if main_data[0]:
        print('Ход игрока №1')
    else:
        print('Ход игрока №2')
    while True:
        coord = input('Введите координаты(Строка:Колонка): ')
        coord = check_coord(coord, len(field))
        if coord:
            # Проверяю заполнена ли клетка
            if field[coord[0]][coord[1]] == '-':
                break
            print('Выбранная клетка заполнена, выберете другую')
    # Заполняю клетку
    field[coord[0]][coord[1]] = 'X' if main_data[0] else 'O'
    print_field(field)
    # Проверка заполненных клеток
    result = check_field(field)
    winner = False
    print(result)
    if not result:
        return not main_data[0], True, field
    # Если кто то выиграл, вывожу поздравление и предложение начать игру заново
    elif result == 1:
        # выиграл первый игрок
        print('Первый игрок выиграл. Поздравляю!!!')
        winner = True
    elif result == 2:
        # выиграл первый игрок
        print('Второй игрок выиграл. Поздравляю!!!')
        winner = True
    elif result == 3:
        print('Поздравляю, у Вас ничья!')
        winner = True
    if winner:
        print('Желаете начать игру заново?')
        answer = input('Введиде "Да" для продолжения: ')
        if answer.lower() == 'да':
            return init_field()
    return not main_data[0], False, field


if __name__ == '__main__':
    setup()
    data = init_field()
    while True:
        data = loop(data)
        if not data[1]:
            break
    print()
    print('Спасибо что играли в эту игру, надеюсь она Вам понравилась')
