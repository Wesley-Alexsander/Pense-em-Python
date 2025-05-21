# um valor é uma representação de um dado, que pode ser
# um número, um texto, uma lista e etc...
# essees valores pertencem a um tipo, que é a forma como o
# computador interpreta esse valor.

# os tipos de valores mais comuns são:
# int: números inteiros
print(type(2))
print(type(1_000_000))  # numeros inteiros com separador de milhar

# float: números decimais
print(type(2.5))
# str: strings, ou seja, textos
print(type("Olá, mundo!"))

# numeros dentro de aspas são considerados strings
print(type("2"))
# o mesmo vale para números decimais
print(type("2.5"))

# Bonus de pesquisa, não listado no livro até o momento:
# bool: booleanos, ou seja, verdadeiro ou falso
print(type(True))
# list: listas, ou seja, uma coleção de valores
print(type([1, 2, 3]))
# tuple: tuplas, ou seja, uma coleção de valores imutável
print(type((1, 2, 3)))
# dict: dicionários, ou seja, uma coleção de pares chave-valor
print(type({"nome": "João", "idade": 30}))
# set: conjuntos, ou seja, uma coleção de valores únicos
print(type({1, 2, 3}))
# frozenset: conjuntos imutáveis, ou seja, uma coleção de valores únicos
print(type(frozenset({1, 2, 3})))
