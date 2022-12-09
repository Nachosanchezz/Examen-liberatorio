def fib(n):                # escribe la serie de Fibonacci hasta n
    a, b = 0,1             # a y b son los dos primeros numeros de la serie
    while a < n:           # mientras a sea menor que n
        print(a, end=' ')      # imprime a
        a, b = b, a+b          # a toma el valor de b y b toma el valor de a+b
    print()                    # imprime un salto de linea
fib(1000000)                   # llama a la funcion fib con el argumento 1000000