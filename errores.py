#!/usr/bin/env python3

def error_absoluto(valor_real : float, valor_aproximado : float) -> float:

    """
    
    Calcula el error absoluto. Mediante una resta del valor real y  el valor aproximado
    devolviendo el valor absoluto de esa resta.
    
    
    return : float
    """


    return abs(valor_real - valor_aproximado)



def error_relativo(error_absoluto: float,valor_real : float) ->  float:

    """
    
    Calcula el error relativo, mediante una division del error absoluto
    entre el valor real, retornando el valor absoluto de esa division.

    El parametro 'valor_real' no puede ser 0.

    return: float
    
    """

    if valor_real == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    else:
        return abs(error_absoluto/valor_real)




if __name__ == "__main__":

    #caso 1

    valor_real = 20_000
    valor_aproximado = 19_999 
    err_abs = error_absoluto(valor_real,valor_aproximado)
    err_re = error_relativo(err_abs,valor_real)
    print(f"Error absoluto: {err_abs}")
    print(f"Error relativo: {err_re}")

    #caso 2

    valor_real = 5
    valor_aproximado = 4

    err_abs = error_absoluto(valor_real,valor_aproximado)
    err_re = error_relativo(err_abs,valor_real)

    print(f"Erro absoluto: {err_abs}")
    print(f"Erro relativo: {err_re}")
