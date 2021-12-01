import math

print("для уравнения ax^2 + bx + c = 0 введите:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c
print(f"дискриминант = {D}")

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("дискриминант отрицательный, корней нет")