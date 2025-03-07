def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Фигура не является треугольником"
    elif a == b == c:
        return "Фигура является равностороним треугольником"
    elif a == b or a == c or b == c:
        return "Фигура является равнобедреным треугольником"
    elif pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2):
        return "Фигура является прямоугольным треугольником"
    else:
        return "Фигура является разностороним треугольником"
