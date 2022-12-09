import sympy
def operacion():
    print("Formula: (a*x*b)**n")
    a = int(input("a: "))            
    b = int(input("b: "))
    x = int(input("x: "))
    n = int(input("n: "))
    operacion = (a*x*b)**n               # a y b son los dos primeros numeros de la serie
    if n == 0:                            # n es 0
        print("El resultado es: 1", 1)     # imprime resultado
    elif n == 1:                             # a toma el valor de b y b toma el valor de a+b
        print("El resultado es: ", operacion)           
    elif n%2 == 0:                            # numero par
        operacion = abs(operacion)
        print("El resultado es: ", operacion)
    else :
        print("El resultado es: ", operacion)
operacion()