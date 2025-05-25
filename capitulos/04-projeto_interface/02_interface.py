"""
Podemos fazer a mesma coisa de forma mais concisa
com uma instrução for.
"""
import turtle

bob = turtle.Turtle()


#  Aqui está uma instrução for que desenha um quadrado:
for i in range(4):
    bob.fd(100)
    bob.lt(90)


turtle.mainloop() # deve sempre vir por ultimo
