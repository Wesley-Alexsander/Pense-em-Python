# variavel é o nome que se dá a um espaço na memória do computador
# que armazena um valor, e tem um tipo e um nome associado a esse valor.
# variaveis são declaradas com o comando "nome_variavel = valor"
# variaveis são mutáveis, ou seja, podem ser alteradas

# Nomes de variaveis devem seguir algumas regras:
# nomes de variáveis não podem começar com números
# e não podem conter espaços ou caracteres especiais, como: @, #, $, %, etc.
# Nomes de variáveis podem conter letras, números e o caractere de sublinhado (_)
# Nomes de variáveis são sensíveis a maiúsculas e minúsculas
# Nomes de variáveis não podem ser palavras reservadas
# Nomes de variáveis devem ser descritivos e significativos

# Instruções de atribuição
#  Uma instrução de atribuição cria uma nova variável e dá
#  um valor a ela:
message = "And now for something completely different"
num = 17
pi = 3.14159

# Esse exemplo faz três atribuições. A primeira atribui uma
#  string a uma nova variável chamada message; a segunda
#  dá o número inteiro 17 a n; a terceira atribui o valor
#  (aproximado) de π a pi

# verificando o tipo da variável
print(type(message))  # <class 'str'>
print(type(num))      # <class 'int'>
print(type(pi))       # <class 'float'>

# expressoes arithmetic com variaveis
#  Uma expressão é uma combinação de valores, variáveis e
#  operadores que o Python pode avaliar para produzir um
#  novo valor.
valor_01 = 10
valor_02 = 20

soma = valor_01 + valor_02
print(soma)  # 30

subtracao = valor_01 - valor_02
print(subtracao)  # -10

# podemos combinar valores armazenads em variáveis com valores
#  literais, como números e strings.
print(valor_01 + 5)  # 15
print(valor_02 - 25)  # 15

# Ordem das operações
#  O Python segue a ordem das operações matemáticas padrão
#  (também conhecida como precedência de operadores) ao
#  avaliar expressões. A ordem das operações é a seguinte:

# 1. Parênteses:
#  Os Parênteses têm a precedência mais alta e podem
#  ser usados para forçar a avaliação de uma expressão
#  na ordem que você quiser. como em (2 + 3) * 4, que é igual a 20.
precedencia = (2 + 3) * 4
print(precedencia)  # 20

# 2. Exponenciação:
#  O operador de exponenciação (**) tem a segunda
#  maior precedência. Ele é usado para elevar um número
#  a uma potência, como em 2 ** 3, que é igual a 8.
potencia = 2 ** 3
print(potencia)  # 8

ordem_precedencia = 2 + 3 * 4  # A multiplicação tem precedência sobre a adição
print(ordem_precedencia)  # 14

# 3. Multiplicação e divisão:
#  Os operadores de multiplicação (*) e divisão (/) têm
#  a mesma precedência e são avaliados da esquerda para a direita.

# Esquerda -> Direita
ex01  = 2 * 3 / 2
print(ex01)  # 3

# Esquerda -> Direita
ex02 = 2 / 3 * 2
print(ex02)  # 1.3333333333333333


# 4. Adição e subtração:
#  Os operadores de adição (+) e subtração (-) têm a
#  mesma precedência e são avaliados da esquerda para a direita.

# Esquerda -> Direita
ex03 = 2 + 3 - 2
print(ex03)  # 3

# Esquerda -> Direita
ex04 = 2 - 3 + 2
print(ex04)  # 1
