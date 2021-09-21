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
def input_matrix():
    matrix = [[input_element()for y in range(n)]for x in range(n)]
    return matrix
def search():
    j = 0
    i = 0
    while j < n:
        if int(matrix[j][j]) <= 0:
            while i < n-1:
                if matrix[j][i-1] < matrix[j][i+1]:
                    min = matrix[j][i-1]
                else:
                    min = matrix[j][i+1]
                i = i + 1
            print(min)
        else:
            print("None")
        j = j + 1
    return 0
n = input_rozmir()
matrix = input_matrix()
for im in range(n):
    print(matrix[im])
search()