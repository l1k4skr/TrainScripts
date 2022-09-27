"""
#? Cualquier digito es seguido de 0
#? Todos los digitos son iguales
#? La secuencia es incremental
  #? el 0 viene despues del 9
#? La secuencia es decremental
    #? el 9 viene despues del 0
#! La secuencia es palindromo 3, 2, 1, 2, 3
#! La secuencia mach con algun valor dentro de la lista de frases_imprecionentantes
"""
def es_seguido_de_0(numero): 
    """Esta funcion debe retornar True si el numero es seguido de 0

    Args:
        numero (_str_): _Numero entregado por el usuario_
    Returns:
        _bool_: _True si el numero es seguido de 0_
    """
    comprobatoria = True
    for i in range(len(numero) - 1, 0, -1):
        if numero[i] == "0":
            comprobatoria = True
        else:
            comprobatoria = False
            break
    return comprobatoria
def son_iguales(numero):
    """Esta funcion debe retornar True si todos los digitos son iguales

    Args:
        _numero_ (_str_): _Numero entregado por el usuario_

    Returns:
        _bool_: _True si todos los valores son iguales _
    """
    return 1 == len(set(numero))
def es_incremental(numero):
    """Comprueba si el numero es incremental

    Args:
        numero (_str_): _numero entregado por el usuaruio_

    Returns:
        _bool_: _True si es incremental_
    """
    numero = list(numero)
    comprobador = False
    for i in range(len(numero)-1):

        if int(numero[i]) == int(numero[i+1])-1 or (int(numero[i]) == 9 and int(numero[i+1]) == 0):
            comprobador = True
        else:
            comprobador = False
            break
    return comprobador
def es_decremental(numero):
    """Comprueba si el numero es decremental

    Args:
        numero (_str_): _numero entregado por el usuaruio_

    Returns:
        _bool_: _True si es decremental_
    numero = list(numero)
    """
    comprobador = False
    for i in range(len(numero)-1):
        if int(numero[i]) == int(numero[i+1])+1 or (int(numero[i]) == 0 and int(numero[i+1]) == 9):
            comprobador = True
        else:
            comprobador = False
            break
    return comprobador
def es_palindromo(numero):
    """Esta funcion debe retornar True si el numero es palindromo

    Args:
        numero (_str_): _Numero entregado por el usuario_

    Returns:
        _bool_: _True si el numero es palindromo_
    """
    return numero == numero[-1::-1]

def main(numero):
    """Funcion para DRY

    Args:
        numero (_str_): _a evaluar_
    """
    return  es_seguido_de_0(numero) or son_iguales(numero) or es_incremental(numero) or es_decremental(numero) or es_palindromo(numero)

def es_interesante(numero, frases_imprecionentantes):
    """Comprobar si el numero es interesante

    Args:
        numero (_Int_): _Numero a evaluar_
        frases_imprecionentantes (_List_): __

    Returns:
        _type_: _description_
    """
    print(numero, frases_imprecionentantes)
    numero = str(numero)
    if int(numero) <= 97:
        return 0
    else:
        if (main(numero) or int(numero) in frases_imprecionentantes )and len(numero) >= 3:
            return 2
        elif main(str(int(numero)+1)) or main(str(int(numero)+2)) or int(numero)+1 in frases_imprecionentantes or int(numero)+2 in frases_imprecionentantes:
            return 1
        else:
            return 0

print(es_interesante(109,[]))