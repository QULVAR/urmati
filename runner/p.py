from sympy import symbols, sympify, expand

z, y = symbols('z y')
s1 = 'x + y'.replace('x', 'z')
s2 = 'x + y'.replace('x', 'z')
print(str(expand(sympify(s1) * sympify(s2))).replace('z', 'x'))