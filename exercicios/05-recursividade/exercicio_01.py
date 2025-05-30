"""
 Exercício 5.2
 O último teorema de Fermat diz que não existem números
 inteiros a, b e c tais que: (a**n + b**n == c**n
 para quaisquer valores de n maiores que 2.
"""

#  1. Escreva uma função chamada check_fermat que
#  receba quatro parâmetros – a, b, c e n – e verifique se o
#  teorema de Fermat se mantém. Se n for maior que 2 e
#  a**n + b**n == c**n o programa deve imprimir, “Holy
#  smokes, Fermat was wrong!” Senão o programa deve
#  exibir “No, that doesn’t work.”


def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print("“Holy smokes, Fermat was wrong!”")
    print("“No, that doesn’t work.”")


# check_fermat(4, 2, 5, 2)

#  2. Escreva uma função que peça ao usuário para digitar
#  valores para a, b, c e n, os converta em números
#  inteiros e use check_fermat para verificar se violam o
#  teorema de Fermat
def check_fermat_inputs():
    a, b, c, n = input("digite algo:\n").split(" ")
    a, b, c, n = int(a), int(b), int(c), int(n)
    if a**n + b**n == c**n:
        print("“Holy smokes, Fermat was wrong!”")
    print("“No, that doesn’t work.”")


# check_fermat_inputs()


def check_fermat_inputs2(a, b, c, n):
    a, b, c, n = int(a), int(b), int(c), int(n)
    if a**n + b**n == c**n:
        print("“Holy smokes, Fermat was wrong!”")
    print("“No, that doesn’t work.”")


# check_fermat_inputs2(*input("digite algo:\n").split(" "))

def check_fermat_inputs3():
    a, b, c, n = map(int, input("Digite 4 valore:\n").split(" "))
    if a**n + b**n == c**n:
        print("“Holy smokes, Fermat was wrong!”")
    # print(f"a={type(a)}, b={type(b)}, b={type(c)}, b={type(n)}")
    print("“No, that doesn’t work.”")


check_fermat_inputs3()
