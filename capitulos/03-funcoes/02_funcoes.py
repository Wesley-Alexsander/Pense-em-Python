# =============================================
# FUNÇÕES PERSONALIZADAS: DEFINIÇÃO E USO
# =============================================

"""
ETAPAS PARA CRIAR UMA FUNÇÃO:
1. Definir nome (descritivo e em snake_case)
2. Definir parâmetros (entre parênteses)
3. Implementar corpo (bloco indentado)
4. Especificar retorno (opcional)
"""

# ---------------------------------------------
# REGRAS DE NOMEAÇÃO:
# ---------------------------------------------
# - Letras minúsculas e underscores (_)
# - Não pode iniciar com números
# - Sem caracteres especiais (@, #, $)
# - Não usar palavras reservadas (if, for)
# - _nome (underline indica uso interno - evitar)

# ---------------------------------------------
# SINTAXE BÁSICA:
# ---------------------------------------------


def cumprimentar(nome):
    """Retorna mensagem personalizada com o nome recebido"""
    return f"Olá, {nome}! Como você está?"


# Verificação do tipo
print(type(cumprimentar))  # <class 'function'>

# Chamadas válidas:
print(cumprimentar("João"))  # Chamada direta
mensagem = cumprimentar("Maria")  # Armazenamento
print(mensagem)

# ---------------------------------------------
# FLUXO DE EXECUÇÃO:
# ---------------------------------------------
# 1. Chamada da função
# 2. Busca da definição
# 3. Passagem de argumentos
# 4. Execução do bloco
# 5. Retorno do valor (se existir)
# 6. Continuação do programa


# ---------------------------------------------
# PARÂMETROS E ESCOPO:
# ---------------------------------------------
def calcular_soma(a, b, c=0):
    """
    Soma três valores com parâmetro opcional:
    - a: primeiro valor (obrigatório)
    - b: segundo valor (obrigatório)
    - c: terceiro valor (padrão=0)
    Retorna string formatada com o resultado
    """
    resultado = a + b + c  # Variável local
    texto = f"A soma de {a}, {b} e {c} é: {resultado}"
    return texto


# Exemplos de chamada:
print(calcular_soma(1, 2, 3))   # Todos os parâmetros
valor = calcular_soma(3.5, 2.5)  # Usando valor padrão
print(valor)  # Exibe resultado

# ---------------------------------------------
# CARACTERÍSTICAS IMPORTANTES:
# ---------------------------------------------
# - Variáveis criadas dentro da função são LOCAIS
# - Parâmetros quando criados, são obrigatórios (a menos que tenham valor padrão)
# - O return encerra a execução imediatamente, e devolve o valor (se não houver, devolve None)
# - Docstrings (entre aspas triplas) documentam a função
# ---------------------------------------------
