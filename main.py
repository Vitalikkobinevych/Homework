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
def input_matrix(n):
    matrix = [[check_int()for y in range(n)]for x in range(n)]
    return matrix
def print_matrix(matrix, n):
    for im in range(n):
        print(matrix[im])
def search():
    n = check_rozmir()
    matrix = input_matrix(n)
    j = 0
    i = 0
    min = 0
    print_matrix(matrix, n)
    while j < n:
        if int(matrix[j][j]) <= 0:
            while i < n:
                if matrix[j][i - 1] < matrix[j][i]:
                    min = matrix[j][i - 1]
                else:
                    min = matrix[j][i]
                i = i + 1
            i = 0
        j = j + 1
    print(min)

def console():
    print("Enter 1 for exit or 2 for repeat")
    n = check_int()
    if n == 2:
        main()
    elif n == 1:
        exit()
    else:
        print("Incorect")
        console()
def main():
    search()
    console()
main()