"""
3. Faça uma cópia do square e mude o nome para
 polygon. Acrescente outro parâmetro chamado n e
 altere o corpo para que desenhe um polígono regular
 de n lados.
"""
import turtle

bob = turtle.Turtle()

# Para isso podemos usar duas formas:
# usando: loop + .forward() + .left()
# ou: .setpos(X, Y)

def polygon(*, T, n, length=100):
    T.pensize(2)
    for _ in range(n):
        T.forward(length)
        T.left(60)
    turtle.mainloop()


# polygon(T=bob, n=6)

# essa função e a de cima são equivalentes
def polygon2(*, T, n, length=100):
    angle = 360 / n
    T.pensize(2)
    for _ in range(n):
        T.forward(length)
        T.left(angle)
    turtle.mainloop()


# polygon2(T=bob, n=6)


# Lembre-se que o turtle usa o plano cartesiano
# para orientação do cursor, se necessário
# use uma imagem de exemplo, para ver para onde os eixos vão
def polygon2(T):
    T.pensize(2)
    T.setpos(100, 0)  # andar 100 px no eixo x
    T.setpos(160, 100)  # andar +60 px no eixo x enquanto sobe no eixo y 100
    T.setpos(100, 200)  # volta -60 px no eixo x enquanto sobe +100 no eixo y
    T.setpos(0, 200)  # volta -100 casa no eixo x enquanto mante o eixo y
    T.setpos(-60, 100)
    T.setpos(0, 0)

    turtle.mainloop()


polygon2(bob)
