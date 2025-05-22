# =============================================
# FUNÇÕES EM PYTHON: CONCEITOS E APLICAÇÕES
# =============================================

# Definição:
# Uma função é um bloco de código nomeado que executa uma operação específica.
# Composta por: nome, parênteses () e argumentos (opcionais).
# sintaxe: nome_da_funcao(argumento1, argumento2, ...)


# ---------------------------------------------
# 1. FUNÇÕES BUILT-IN (INTEGRADAS)
# ---------------------------------------------

# Exemplo 1: print()
# - Função: Saída de dados no console
# - Argumento: String "Olá, Mundo!"
print("Olá, Mundo!")  # Executa a função

# Exemplo 2: type()
# - Função: Retorna o tipo do objeto
# - Argumento: Valor numérico 10
# - Retorno: Tipo 'int' (inteiro)
tipo = type(10)
print(tipo)  # <class 'int'>

# ------------------------------------------------
# 2. FUNÇÕES DE BIBLIOTECAS (MÓDULOS) - Built-in
# ------------------------------------------------
import math  # Importa o módulo matemático

# Estrutura: modulo.funcao(argumento)

# Exemplo 3: math.sqrt()
# - Calcula a raiz quadrada
# - Argumento: Número 16
# - Retorno: 4.0 (float)
raiz = math.sqrt(16)
print(raiz)  # 4.0

# Verificação do tipo da função
print(type(math.sqrt))  # <class 'builtin_function_or_method'>

# ---------------------------------------------
# 3. APLICAÇÕES PRÁTICAS
# ---------------------------------------------

# Caso 1: Cálculo de SNR (Decibéis)
# Fórmula: SNR(dB) = 10 * log10(P_sinal/P_ruido)
P_sinal = 1000  # Potência do sinal (W)
P_ruido = 100   # Potência do ruído (W)

snr_db = 10 * math.log10(P_sinal / P_ruido)
print(f"SNR: {snr_db:.2f} dB")  # 10.00 dB

# ---------------------------------------------------
# Caso 2: Cálculo Trigonométrico (Graus → Radianos)
# ---------------------------------------------------
angulo = 45  # Ângulo em graus

# Método 1: Conversão manual
radianos1 = angulo * (math.pi / 180)

# Método 2: Função math.radians() (otimizado)
radianos2 = math.radians(angulo)

# Cálculo do seno (ambos métodos equivalem)
seno1 = math.sin(radianos1)
seno2 = math.sin(radianos2)

print(f"Seno de {angulo}°: {seno1:.2f}")  # 0.71

# ---------------------------------------------
# 4. COMPOSIÇÃO DE FUNÇÕES
# ---------------------------------------------

# Exemplo: Expressão matemática aninhada
# e^(ln(x+1)) usando math.exp() e math.log()
x = 2
resultado = math.exp(math.log(x + 1))  # Retorna 3.0

# =============================================
# PRÓXIMOS PASSOS:
# - Criação de funções personalizadas
# - Parâmetros e valores de retorno
# =============================================
