from functions import *


def main():
    apart('Visualizador de Formas Geométicas', 46)
    form()
    while True:
        choice = select_form('[Quadrado] [Losango] [Triangulo]: ')
        if choice == 'quadrado':
            side = select_side('qua')
            print_qua(side)
        if choice == 'losango':
            side = select_side('los')
            print_los(side)
        if choice == 'triangulo':
            form_tri()
            while True:
                tri = int(input('Selecione o Triângulo: '))
                if tri == 1:
                    side = select_side('tri_1')
                    print_tri_1(side)
                    break
                if tri == 2:
                    side = select_side('tri_2')
                    print_tri_2(side)
                    break
                else:
                    print('\033[31mDado Inválido, Tente Novamente!!\033[m')
                    continue
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print()
        if cont == 'N':
            break
    apart('Fim do Programa, Volte Sempre!!!', 41)


if __name__ == '__main__':
    main()
