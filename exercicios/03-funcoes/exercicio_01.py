# 1. Escreva uma função que desenhe uma grade como a
#  seguinte:
#     + - - - - + - - - - +
#     |         |         |
#     |         |         |
#     |         |         |
#     |         |         |
#     + - - - - + - - - - +
#     |         |         |
#     |         |         |
#     |         |         |
#     |         |         |
#     + - - - - + - - - - +
#  Dica: para exibir mais de um valor em uma linha,
#  podemos usar uma sequência de valores separados
#  por vírgula: #  print('+', '-')
#  Por padrão, print avança para a linha seguinte, mas
#  podemos ignorar esse comportamento e inserir um
#  espaço no fim, desta forma: python print('+', end=' ')
#  print('-')
#  A saída dessas instruções é +- Uma instrução print
#  sem o argumento "terminar a linha atual"


def grade():
    print('+' + ' -' * 4, '+ ' + ' -' * 4, '+')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('+' + ' -' * 4, '+ ' + ' -' * 4, '+')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('|' + ' ' * 8, '|', ' ' * 8, '|')
    print('+' + ' -' * 4, '+ ' + ' -' * 4, '+')


grade()


def grade2():
    print((' +' + ' -' * 4) * 2, "+")
    print(((" |" + " " * 8) * 3 + "\n") * 4, end="")
    print((' +' + ' -' * 4) * 2, "+")
    print(((" |" + " " * 8) * 3 + "\n") * 4, end="")
    print((' +' + ' -' * 4) * 2, "+")


grade2()


#  2. Escreva uma função que desenhe uma grade
#  semelhante com quatro linhas e quatro colunas.

def grade3(contador):
    print((' +' + ' -' * 4) * 4, "+")
    print(((" |" + " " * 8) * 5 + "\n") * 4, end="")
    print((' +' + ' -' * 4) * 4, "+")
    print(((" |" + " " * 8) * 5 + "\n") * 4, end="")

    if contador < 1:
        grade3(contador + 1)  
        print((' +' + ' -' * 4) * 4, "+")

grade3(0)  # função recursiva
