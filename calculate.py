from sympy.abc import x
from sympy import Poly, Intersection
from sympy.solvers.inequalities import solve_poly_inequality

with open('input.txt', 'r') as f:
    b11, b21, b12, b22, a11, a21, a12, a22 = [int(a) for a in f.read().split()]

C = a11 - a12 - a21 + a22
a = a22- a12
D = b11 - b12 - b21 + b22
b = b22 - b21

p1 = solve_poly_inequality(Poly(C * x - a), '>=')[0]
p0 = solve_poly_inequality(Poly(-(C * x - a)), '>=')[0]

q1 = solve_poly_inequality(Poly(D * x - b), '>=')[0]
q0 = solve_poly_inequality(Poly(-(D * x - b)), '>=')[0]

with open('output.txt', 'w') as f:
    f.write("Оптимальные стратегии по Нэшу:\n")
    f.write("P* = ({}; {})\n".format(Intersection(q1, q0).sup, abs(Intersection(q1, q0).sup - 1)))
    f.write("Q* = ({}; {})\n".format(Intersection(p1, p0).sup, abs(Intersection(p1, p0).sup - 1)))
