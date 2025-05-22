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

# Resultados
print(f"Passo médio: {minutos} minutos e {segundos} segundos por milha")
print(f"Velocidade média: {velocidade_mph:.2f} milhas por hora")
