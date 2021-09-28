def check_int():
    try:
        x = int(input("Введіть число "))
    except ValueError:
        print("Invalid value")
        print("Must be number ")
        return check_int()
    return x
def check_rozmir():
    n = check_int()
    if n <= 0:
        print("Number must be > 0 ")
        return check_rozmir()
    return n
def input_matrix():
    matrix = [[check_int()for y in range(n)]for x in range(n)]
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
n = check_rozmir()
matrix = input_matrix()
for im in range(n):
    print(matrix[im])
search()