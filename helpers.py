def solve_quadratic_eq(a, b, c):
    if a == 0:
        x = -c/b
        return (x,)
    delta = b**2 - 4*a*c
    if delta < 0:
        return tuple()
    if delta == 0:
        x = -b / (2*a)
        return (x,)
    if delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2