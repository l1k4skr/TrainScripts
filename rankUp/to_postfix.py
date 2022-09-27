def to_postfix(infix):
    """Converts an infix expression to postfix.
    
    args:
        infix: a string containing an infix expression
    returns:
        a string containing the postfix expression
    """
    operadores = []
    numeros = []
    for i in infix:
        if i in "0123456789":
            numeros.append(i)
        elif i in "+-*/^":
            operadores.append(i)
        elif i == ")":
            numeros.append(operadores.pop())
        elif i == "(":
            pass
        else:
            raise ValueError("Invalid character: {}".format(i))
    for i in range(len(operadores)-1, -1, -1):
        numeros.append(operadores[i])
    return "".join(numeros)

print(to_postfix("(1*(2-3))+(4+5)"))