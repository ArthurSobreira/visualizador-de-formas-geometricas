from time import *


def apart(txt, color, size=50):
    print('\033[97;1m=\033[m' * size)
    print(f'\033[{color};1m{txt:^{size}}\033[m')
    print('\033[97;1m=\033[m' * size)


def form():
    print('\033[36;1m      *  *  *          *              *\n'
          '      *  *  *       *  *  *         *   *\n'
          '      *  *  *          *          *   *   *')


def form_tri():
    print('\033[97;1m=\033[m' * 50)
    print('  \033[97m(1)\033[m \033[36;1m*               \033[97m(2)\033[m     \033[36;1m*\n'
          '      *  *                  *   *\n'
          '      *  *  *             *   *   *\033[m')
    print('\033[97;1m=\033[m' * 50)


def select_form(msg):
    apart('Selecione a forma que deseja visualizar', 46)
    while True:
        try:
            choice = str(input(msg)).strip().lower()
        except (ValueError, TypeError):
            print('\033[31mDado Inválido, Tente Novamente!!\033[m')
            continue
        else:
            if choice in ['quadrado', 'losango', 'triangulo']:
                return choice
            else:
                print('\033[31;1mDado Inválido, Tente Novamente!!\033[m')
                continue


def select_side(form):
    while True:
        try:
            val = int(input('Digite o valor do lado: '))
        except (ValueError, TypeError):
            print('\033[31mDado Inválido, Tente Novamente!!\033[m')
            continue
        else:
            if val < 2:
                print('\033[31mNão é possível visualizar uma forma com o lado passado!!\033[m')
                continue
            else:
                if (form == 'tri_2') or (form == 'los'):
                    if val % 2 == 0:
                        print('\033[31mDado Inválido, apenas valores ímpares permitidos!!\033[m')
                        continue
                    else:
                        return val
                else:
                    return val


def print_qua(side):
    print()
    if side > 16:
        size = side * 3
    else:
        size = 50
    apart('Visualizando o Quadrado', 97, size)
    for c in range(side):
        for i in range(side):
            print(' \033[32m*\033[m ', end='')
        print()
        sleep(0.3)
    print('\033[97;1m=\033[m' * size)


def print_los(side):
    print()
    if side > 12:
        size = side * 4
    else:
        size = 50
    apart('Visualizando o Losango', 97, size)
    # Lado de cima
    esp = side
    sym = 1
    for c in range(side - 1):
        print('  ' * esp, end='')
        for i in range(sym):
            print('\033[32m*\033[m', end='   ')
        print()
        sleep(0.3)
        sym += 1
        esp -= 1

    # Lado de baixo
    esp = 1
    sym = side
    for c in range(side):
        print('  ' * esp, end='')
        for i in range(sym):
            print('\033[32m*\033[m', end='   ')
        print()
        sleep(0.3)
        sym -= 1
        esp += 1
    print('\033[97;1m=\033[m' * size)


def print_tri_1(side):
    print()
    if side > 16:
        size = side * 3
    else:
        size = 50
    apart('Visualizando o Triangulo 1', 97, size)
    for c in range(1, (side + 1)):
        print(' \033[32m*\033[m ' * c, end='')
        print()
        sleep(0.3)
    print('\033[97;1m=\033[m' * size)


def print_tri_2(side):
    print()
    if side > 12:
        size = side * 4
    else:
        size = 50
    apart('Visualizando o Triangulo 2', 97, size)
    esp = side
    sym = 1
    for c in range(side):
        print('  ' * esp, end='')
        for i in range(sym):
            print('\033[32m*\033[m', end='   ')
        print()
        sleep(0.3)
        sym += 1
        esp -= 1
    print('\033[97;1m=\033[m' * size)

