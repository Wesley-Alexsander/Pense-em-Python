"""
Este capítulo apresenta um estudo de caso que
demonstra o processo de criação de funções que operam
simultaneamente.

Ele apresenta o módulo turtle, que permite criar imagens
usando [turtle graphics][1].
"""
import turtle


def turtle_basic_configs():
    """ Possíveis formatos:
            -> arrow (seta)
            -> blank (invisível)
            -> circle (círculo)
            -> classic (clássica)
            -> square (quadrado)
            -> triangle (triângulo)
            -> turtle (tartaruga)

        Encontrar mais opções de cores:
            - https://trinket.io/docs/colors
    """
    bob = turtle.Turtle()  # instanciar/criar um objeto turtle interface
    bob.shape("turtle")  # mudar a apararencia do cursor
    bob.color("medium aquamarine")  # altera a cor do cursor
    turtle.mainloop()  # mantém a janela aberta até o usuario fecha-la


# turtle_basic_configs()


def turtle_mover_para_frente():
    """
    bob.fd(100) ou bob.forward(100) --> mover 100 de distances em pixels para frente
    bob.bk(100) ou bob.back(100) --> mover 100 de distances em pixels para trás
    bob.lt(90)  ou bob.left(100) --> virar a seta a esquerda
    bob.rt(90)  ou bob.right(100) --> virar a seta a direita

    bob.setpos(100, 100) --> movimenta a tartaruga para a posição específica em x e y.
    """
    bob = turtle.Turtle()

    bob.shape("turtle")
    bob.color("medium aquamarine")

    bob.forward(100)

    turtle.mainloop()


# turtle_mover_para_frente()


def turtle_mover_para_tras():
    """
    bob.fd(100) ou bob.forward(100) --> mover 100 de distances em pixels para frente
    bob.bk(100) ou bob.back(100) --> mover 100 de distances em pixels para trás
    bob.lt(90)  ou bob.left(100) --> virar a seta a esquerda
    bob.rt(90)  ou bob.right(100) --> virar a seta a direita

    bob.setpos(100, 100) --> movimenta a tartaruga para a posição específica em x e y.
    """
    bob = turtle.Turtle()

    bob.shape("turtle")
    bob.color("medium aquamarine")

    bob.back(100)

    turtle.mainloop()


# turtle_mover_para_tras()


def turtle_mover_para_frente_e_virar_para_esqueda():
    """
    bob.fd(100) ou bob.forward(100) --> mover 100 de distances em pixels para frente
    bob.bk(100) ou bob.back(100) --> mover 100 de distances em pixels para trás
    bob.lt(90)  ou bob.left(100) --> virar a seta a esquerda (parametro: angulo)
    bob.rt(90)  ou bob.right(100) --> virar a seta a direita (parametro: angulo)

    bob.setpos(100, 100) --> movimenta a tartaruga para a posição específica em x e y.
    """
    bob = turtle.Turtle()

    bob.shape("turtle")
    bob.color("medium aquamarine")

    bob.forward(100)
    bob.left(90)  # vira 90º para a esquerda

    turtle.mainloop()


# turtle_mover_para_frente_e_virar_para_esqueda()


def turtle_desenhando_quadrado():
    bob = turtle.Turtle()

    bob.shape("turtle")
    bob.color("medium aquamarine")

    bob.fd(100)  # andar 100 pixel para frente
    bob.lt(90)  # vira 90º para a esquerda
    bob.fd(100)  # andar 100 pixel para frente
    bob.lt(90)  # vira 90º para a esquerda
    bob.fd(100)  # andar 100 pixel para frente
    bob.lt(90)  # vira 90º para a esquerda
    bob.fd(100)  # andar 100 pixel para frente

    turtle.mainloop()


turtle_desenhando_quadrado()
