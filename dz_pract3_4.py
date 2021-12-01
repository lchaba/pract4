
print("для уравнения ax^2 + bx + c = 0 введите:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c
print(f"дискриминант = {D}")

if D == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))