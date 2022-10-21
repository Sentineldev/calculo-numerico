#!/usr/bin/env python3




def existe_valor_intermedio(f, x: float, y: float) -> bool:

    """
    Se toma una funcion matematica cualquiera
    i.e: x^2 - 4 continua
    y  un intervalo (x,y).
    donde si el producto, de evaluar ambos valores en esa funcion
    es < 0 existe un valor p  en el intervalo, tal que f(p) es = 0.

    return : bool

    """

    return (f(x) * f(y)) < 0    




def es_numero_raiz(f,x) -> bool:

    """
    Se evalua si el valor dado 
    evaluado en la funcion
    es raiz de de la funcion.
    
    return : bool

    """

    return f(x) == 0


if __name__ == "__main__":

    f = lambda x: x**2 - 4

    a = 0
    b = 5



    #casos de prueba.    
    print(f"Existe valor intermedio: {existe_valor_intermedio(f,a,b)}")



    print(f"Es numero raiz: {es_numero_raiz(f,2)}")
    print(f"Es numero raiz: {es_numero_raiz(f,-2)}")
    print(f"Es numero raiz: {es_numero_raiz(f,4)}")
    print(f"Es numero raiz: {es_numero_raiz(f,4)}")
