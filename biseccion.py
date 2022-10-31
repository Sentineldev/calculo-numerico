import math





def biseccion(funcion,intervalo:tuple,error_relativo : float,num_iteraciones:int):


    """
    variables que funcionan como puntos de break del cciclo while.
    
    """
    error_relativo_aproximado = 100
    num_iteraciones_actual = 1

    intervalo_a = intervalo[0]
    intervalo_b = intervalo[1]

    aux_previo = 0
    aproximacion_raiz = 0


    """
    El ciclo while funcionara mientras el el numero de iteraciones sea menor al pasado por parametros
    o el error relativo llegue a su objetivo.
    
    """

    while (num_iteraciones_actual < num_iteraciones) and (error_relativo_aproximado > error_relativo):

        
        aux_previo = aproximacion_raiz
        aproximacion_raiz = (intervalo_a+intervalo_b)/2
        

        """
        Eligiendo el nuevo intervalo una vez divida la adicion de la aproximacion.
        """

        if (funcion(intervalo_a) * funcion(aproximacion_raiz)) < 0 :
            intervalo_b = aproximacion_raiz
        else:
            intervalo_a = aproximacion_raiz
        
        if num_iteraciones_actual > 1:
            error_relativo_aproximado = abs((aproximacion_raiz - aux_previo)/aproximacion_raiz)*100


        num_iteraciones_actual+=1



    return (num_iteraciones_actual,error_relativo_aproximado)

        
    
       
