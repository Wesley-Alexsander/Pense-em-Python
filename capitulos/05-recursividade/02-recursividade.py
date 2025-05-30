"""
Quando estamos lidando com funções recursivas,
é importante ter um caso base que interrompa a recursão.
para evitar loops infinitos.

casos base são condições que, quando atendidas,
fazem com que a função retorne um valor sem chamar a si mesma novamente,
finalizando a recursão.
"""


def repetir(texto, vezes):
    if vezes <= 0:
        return  # Caso base: se vezes for menor ou igual a zero, não faz nada
    else:
        print(texto, vezes)
        repetir(texto, vezes - 1)


repetir("Python é legal", 2)


# Recursividade infinita
# Na maior parte dos ambientes de programação, um programa com recursividade
# infinita não é realmente executado para sempre. O python por exemplo,
# irá gerar um erro de RecursionError após atingir o limite máximo de 1000
# recursões.
def recursividade_infinita():
    print("Esta função chama a si mesma indefinidamente.")
    recursividade_infinita()  # Chamada recursiva sem caso base

# recursividade_infinita()  # Descomente para ver o loop infinito
