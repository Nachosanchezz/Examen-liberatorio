from sympy import expand, symbols 
import sympy
x, y, a, b, n = sympy.symbols("x y a b n")
formula = (a*x*b)^n
gfg_exp = expand(formula)
print(gfg_exp)
if a == 1:
    a = 1
elif a == -1:
    a = -1









