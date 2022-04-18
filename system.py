from functions import *

apart('Visualizador de Formas Geométricas')
print('Dados para visualizar o Triângulo:')
print()
while True:
    x = validateTrng('Vértice no eixo X: ')
    y = validateTrng('Vértice no eixo Y: ')
    if x == y:
        break
    print('\033[31mÉ necessário que os vértices possuam o mesmo valor.\033[m')
print()
z = validateDmd('Dados para visualizar o Losango: ')
print()
print('======== Triângulo Retângulo ========')
printTrng(x)
print('============ Losango ============ ')
printDmd(z)
apart('Fim do Programa, Volte Sempre!!')
