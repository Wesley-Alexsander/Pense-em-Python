"""
Uma função pode chamar outra função, mas também pode chamar a si mesma.
Isso é chamado de recursão. A recursão é uma técnica poderosa que pode
simplificar a solução de problemas complexos, dividindo-os em subproblemas
menores e mais gerenciáveis.
"""

# Exemplo de função recursiva:


def countdown(n):
    if n <= 0:
        print("Contagem regressiva concluída!")
    else:
        print(n)
        countdown(n - 1)


# Basicamente, a função countdown imprime o número atual e chama a si mesma
# com o número decrementado em 1, até que o número seja menor ou igual a 0.
countdown(5)


# Uma caracteistica interessante destas funções é que
# ela aguarda a processamento da chamada recursiva antes de continuar
# com o restante do código. Isso significa que a função não retorna
# até que todas as chamadas recursivas tenham sido concluídas.
# Exemplo de função recursiva para calcular o fatorial de um número:
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        # antes de retornar o resultado, aguardamos o resultado da chamada
        # de todas as recursões anteriores
        return n * fatorial(n - 1)


# Exemplo de uso da função fatorial
numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
