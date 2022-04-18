def apart(txt):
    size = len(txt) + 10
    print('=' * size)
    print(f'{txt:^{size}}')
    print('=' * size)


def validateTrng(txtVal):
    while True:
        try:
            val = int(input(txtVal))
        except (ValueError, TypeError):
            print('\033[31mDado inválido, tente novamente.\033[m')
            continue
        else:
            if val >= 2:
                break
            else:
                print('\033[31mNão é possível representar um triângulo com o valor dado.\033[m')
                continue
    return val


def validateDmd(txtVal):
    while True:
        try:
            val = int(input(txtVal))
        except (ValueError, TypeError):
            print('\033[31mDado inválido, tente novamente.\033[m')
        else:
            if not val % 2 == 0:
                break
            else:
                print('\033[31mNão é possível construir um Losango com o valor dado.\033[m')
                continue
    return val


def printTrng(x):
    for c in range(0, x):
        for i in range(0, c + 1):
            print('*', end='  ')
        print()


def printDmd(z):
    space = z // 2
    symbols = z % 2
    for c in range(0, z):
        print('  ' * space, end='')
        print(' *' * symbols, end='')
        print()
        space -= 1
        symbols += 2
        if symbols > z:
            break
    space = 1
    symbols = z - 2
    for c in range(0, z):
        print('  ' * space, end='')
        print(' *' * symbols, end='')
        print()
        space += 1
        symbols -= 2
