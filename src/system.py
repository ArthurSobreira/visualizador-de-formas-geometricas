from functions import *


def main():
    apart('Visualizador de Formas Geométricas')
    print('Dados para visualizar o Triângulo:')
    print()
    while True:
        x = validate_trng('Vértice no eixo X: ')
        y = validate_trng('Vértice no eixo Y: ')
        if x == y:
            break
        print('\033[31mÉ necessário que os vértices possuam o mesmo valor.\033[m')
    print()
    z = validate_dmd('Dados para visualizar o Losango: ')
    print()
    print('======== Triângulo Retângulo ========')
    print_trng(x)
    print('============== Losango ============== ')
    print_dmd(z)
    apart('Fim do Programa, Volte Sempre!!')


if __name__ == '__main__':
    main()
