import sympy as sp
x,y,r = sp.symbols("x y r")
equation1 = sp.Eq(2*x**2 + 3*y**2, r)
equation2 = sp.Eq(y, 2*x + 1)
sol = sp.solve((equation1, equation2), (x, y), dict=True)
print("symbolic solutions are:")
print(sol)

