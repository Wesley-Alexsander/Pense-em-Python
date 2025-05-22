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
