"""
 2. Acrescente outro parâmetro, chamado length, ao
 square. Altere o corpo para que o comprimento dos
 lados seja length e então altere a chamada da função
 para fornecer um segundo argumento. Execute o
 programa novamente. Teste o seu programa com
 uma variedade de valores para length
"""
import turtle

bob = turtle.Turtle()


def square(T, length):
    for _ in range(4):
        T.forward(length)
        T.left(90)
    turtle.mainloop()

square(bob, length=100)