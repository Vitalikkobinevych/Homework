import random
def check_int():
    try:
        x = int(input("Введіть число "))
    except ValueError:
        print("Неправильне значення")
        print("Повинне бути число ")
        return check_int()
    return x
def check_rozmir():
    n = check_int()
    if n <= 0:
        print("Число має бути більше 0 ")
        return check_rozmir()
    return n
def check_diapazon():
    A = check_int()
    B = check_int()
    if A >= B:
        print("Ліва границя повинна бути меншою за праву ")
        return check_diapazon()
    return A, B
def method_1():
    print("Введіть розмір матриці ")
    n = check_rozmir()
    print("Введіть елементи матриці ")
    matrix_1 = [[check_int() for y in range(n)] for x in range(n)]
    return matrix_1
def method_2():
    print("Введіть розмір матриці ")
    N = check_rozmir()
    print("Введіть діапазон значень ")
    A, B = check_diapazon()
    matrix_2 = [[random.randrange(A, B) for y in range(N)]for x in range(N)]
    for im in range(N):
        print(matrix_2[im])
    return matrix_2

def sort(matrix_2):
    i = 0
    j = 0
    k = 0
    arr = []
    N = len(matrix_2)
    while i < len(matrix_2):
        while j < len(matrix_2):
            arr.append(matrix_2[i][j])
            j = j + 1
        j = 0
        i = i + 1

    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    i = 0
    j = 0

    while i < len(matrix_2):
        while k < N:
            matrix_2[i][j] = arr[k]
            k = k + 1
            j = j + 1
        j = 0
        N = N + len(matrix_2)
        i = i + 1
    print("-------")
    for im in range(len(matrix_2)):
        print(matrix_2[im])

def main():
    matrix_1 = method_1()
    matrix_2 = method_2()
    sort(matrix_1)
    sort(matrix_2)
    print("Enter 1 for exit or 2 for repeat")
    n = check_int()
    if n == 2:
        main()
    elif n ==1:
        exit()
    else:
        print("Incorect")
        exit()
main()