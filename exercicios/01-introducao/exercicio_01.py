# Exercício 1.1
#  1. Em uma instrução print, o que acontece se você
#  omitir um dos parênteses ou ambos?

# print("Gera um erro de sintaxe)

#  2. Se estiver tentando imprimir uma string, o que
#  acontece se omitir uma das aspas ou ambas?

# print(Gera um erro de sintaxe)

#  3. Você pode usar um sinal de menos para fazer um
#  número negativo como -2. O que acontece se puser
#  um sinal de mais antes de um número? E se escrever
#  assim: 2++2?

# print(2 + 2)  # Gera um erro de sintaxe

#  4. Na notação matemática, zeros à esquerda são
#  aceitáveis, como em 02. O que acontece se você
#  tentar usar isso no Python?

# print(02) # Gera um erro de sintaxe


# 5. O que acontece se você tiver dois valores sem
#  nenhum operador entre eles?

# print(2 2) # Gera um erro de sintaxe

#  Exercício 1.2
#  Inicialize o interpretador do Python e use-o como uma
#  calculadora.
#  1. Quantos segundos há em 42 minutos e 42 segundos?
print(42 * 60 + 42)  # 2562

#  2. Quantas milhas há em 10 quilômetros? Dica: uma
#  milha equivale a 1,61 quilômetro.
print(10 / 1.61)  # 6.2137

#  3. Se você correr 10 quilômetros em 42 minutos e 42
#  segundos, qual é o seu passo médio (tempo por
#  milha em minutos e segundos)? Qual é a sua
#  velocidade média em milhas por hora?


# Dados do problema
distancia_km = 10
tempo_minutos = 42
tempo_segundos = 42

# 1. Converter tempo total para horas
tempo_total_horas = (tempo_minutos + tempo_segundos/60) / 60

# 2. Converter km para milhas (1 km = 0.621371 milhas)
distancia_milhas = distancia_km / 1.61

# 3. Calcular velocidade média (milhas/hora)
velocidade_mph = distancia_milhas / tempo_total_horas

# 4. Calcular passo médio (minutos/milha)
passo_total_minutos = tempo_minutos + tempo_segundos/60
passo_por_milha = passo_total_minutos / distancia_milhas

# Converter para minutos e segundos
minutos = int(passo_por_milha)
segundos = int((passo_por_milha - minutos) * 60)

# breakpoint()
# Resultados
print(f"Passo médio: {minutos} minutos e {segundos} segundos por milha")
print(f"Velocidade média: {velocidade_mph:.2f} milhas por hora")
