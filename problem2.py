import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from problem1 import x, y, sol

r_value = 10
y_line = 2 * x + 1
ellipse_eq = sp.Eq(2 * x**2 + 3 * y**2, r_value)
y_solutions = sp.solve(ellipse_eq, y)
function1 = sp.lambdify(x, y_solutions[0], "numpy")
function2 = sp.lambdify(x, y_solutions[1], "numpy")
line_func = sp.lambdify(x, y_line, "numpy")
x_vals = np.linspace(-3, 3, 400)
plt.plot(x_vals, function1(x_vals), label="elipse (upper)", color="blue")
plt.plot(x_vals, function2(x_vals), label="elipse (lower)", color="blue")

plt.plot(x_vals,line_func(x_vals), label="Line y = 2x+1", color="red")
sol_num = [{x: s[x].subs("r", r_value).evalf(), y: s[y].subs('r', r_value).evalf()} for s in sol]
for s in sol_num:
    plt.plot(float(s[x]), float(s[y]), 'ko', markersize=8, label="Intersection" if s == sol_num[0] else "")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Elipse and line for r= 10")
plt.xlim(-3,3)
plt.ylim(-5,5)
plt.legend()
plt.grid(True)
plt.savefig("Problem2.pdf")
plt.show



