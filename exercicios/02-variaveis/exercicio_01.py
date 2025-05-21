#  Pratique o uso do interpretador do Python como uma
#  calculadora:

#  1. O volume de uma esfera com raio r é  . Qual é o
#  volume de uma esfera com raio 5?

# formula: V = (4/3) * π * (r ** 3)
volume = (4/3) * 3.14 * (5 ** 3)
print(f"volume do circulo: {volume:.2f}")

#  2. Suponha que o preço de capa de um livro seja
#  R$ 24,95, mas as livrarias recebem um desconto de
#  40%. O transporte custa R$ 3,00 para o primeiro
#  exemplar e 75 centavos para cada exemplar
#  adicional. Qual é o custo total de atacado para 60
#  cópias?
capa = 24.95
desconto = 0.40
transporte_unidade = 3.00
acrecimo_transporte = 0.75
quantidade = 60

custo_final = capa * (1 - desconto) * quantidade + \
    transporte_unidade + (acrecimo_transporte * (quantidade - 1))

print(f"Custo final da entrega: {custo_final:.2f}")

#  3. Se eu sair da minha casa às 6:52 e correr 1
#  quilômetro a um certo passo (8 min 15s por
#  quilômetro), então 3 quilômetros a um passo mais
#  rápido (7min12s por quilômetro) e 1 quilômetro no
#  mesmo passo usado em primeiro lugar,  que horas
#  chego em casa para o café da manhã?

# Dados de entrada
horario_saida = 6
minuto_saida = 52

passo_minuto = 8
passo_segundo = 15
km_passo_lento = 1  # 1 km no ritmo lento

passo_minuto_rapido = 7
passo_segundo_rapido = 12
km_passo_rapido = 3  # 3 km no ritmo rápido

# 1. Converter horário de saída para minutos totais
horario_saida_minutos = (horario_saida * 60) + minuto_saida
# print(f"Horário de saída em minutos: {horario_saida_minutos}")

# 2. Calcular tempo por km em SEGUNDOS
passo_lento_por_km = passo_minuto * 60 + passo_segundo  # 495 seg/km
passo_rapido_por_km = passo_minuto_rapido * 60 + passo_segundo_rapido  # 432 seg/km
# print(f"Tempo por km (lento): {passo_lento_por_km} segundos/km")
# print(f"Tempo por km (rápido): {passo_rapido_por_km} segundos/km")

# 3. Tempo total em SEGUNDOS
tempo_total_segundos = ((km_passo_lento * 2) * passo_lento_por_km) + (km_passo_rapido * passo_rapido_por_km)
# print(f"Tempo total em segundos: {tempo_total_segundos}")

# 4. Converter segundos para minutos
tempo_total_minutos = tempo_total_segundos / 60
# print(f"Tempo total em minutos: {tempo_total_minutos}")

# 5. Calcular horário de chegada
horario_chegada_minutos = horario_saida_minutos + tempo_total_minutos
hora_chegada = int(horario_chegada_minutos // 60)
minuto_chegada = int(horario_chegada_minutos % 60)

print(f"Horário de chegada: {hora_chegada}:{minuto_chegada:02d}")