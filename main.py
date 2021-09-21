import random
def input_rozmir():
    try:
        n = int(input("Введіть розмір матриці: "))
    except ValueError:
        print("Неправильне значення ")
        input_rozmir()
    if n < 1:
        print("Розмір має бути більше 0 ")
        input_rozmir()
    return n
def input_element():
    try:
        element = int(input("Введіть елемент матриці: "))
    except ValueError:
        print("Неправильне значення ")
        input_element()
    return element
def method_1():
    n = input_rozmir()
    matrix_1 = [[input_element() for y in range(n)] for x in range(n)]
    for im in range(n):
        print(matrix_1[im])
    return matrix_1
def input_diapazon():
    try:
        x = int(input("Enter size"))
    except ValueError:
        print("Invalid value")
        input_diapazon()
    return x
def method_2():
    N = input_rozmir()
    A = input_diapazon()
    B = input_diapazon()
    if A >= B:
        A = input_diapazon()
        B = input_diapazon()
    matrix_2 = [[random.randrange(A, B) for y in range(N)]for x in range(N)]
    for im in range(N):
        print(matrix_2[im])
    return matrix_2
method_1()
method_2()