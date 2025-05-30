"""
1. Escreva uma função chamada square que receba um
 parâmetro chamado t, que é um turtle. Ela deve usar
 o turtle para desenhar um quadrado.
 Escreva uma chamada de função que passe bob
 como um argumento para o square e então execute o
 programa novamente
"""
import turtle

bob = turtle.Turtle()


def square(T):
    for _ in range(4):
        T.forward(100) 
        T.left(90)
    turtle.mainloop()


square(bob)


