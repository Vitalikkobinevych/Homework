# def suma_1(n1, n2, n3):
#     sum_1 = n1 + n2
#     sum_2 = n1 + n3
#     sum_3 = n2 + n3
#     print(sum_1, sum_2, sum_3, sep="\n")

def rozryady(n):
    i = 1
    k = 0
    while k < len(str(n)):
        rozryad = int((n % (i * 10) / i))
        k = k + 1
        i = i * 10
        print(rozryad)
# def func(n1, n2):
#     y = rozryady(n1) + rozryady(n2)
#     return str(y[5] + y[2]) + str(y[1] + y[4]) + str(y[0] + y[3])
#
# def suma_2(n1, n2, n3):
#     sum_x = func(n1, n2)
#     sum_y = func(n1, n3)
#     sum_z = func(n2, n3)
#     print(sum_x), print(sum_y), print(sum_z)

def int_input_array(m = ""):
    try:
        numbers = (input().split(" "))
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Enter 3 numbers with a space")
        return int_input_array(m)
    if (len(numbers) < 3):
        return int_input_array(m)
    return numbers
def main():
    print("Enter your numbers")
    n = int_input_array()
    # suma_1(n[0], n[1], n[2])
    print("-----------------")
    #suma_2(n[0], n[1], n[2])
    # print(rozryady(n[0]))
    # print(rozryady(n[1]))
    # print(rozryady(n[2]))
    print(n)
main()
# def suma_1(n1, n2, n3):
#     sum_1 = n1 + n2
#     sum_2 = n1 + n3
#     sum_3 = n2 + n3
#     print(sum_1, sum_2, sum_3, sep="\n")

def rozryady(n):
    i = 1
    k = 0
    while k < len(str(n)):
        rozryad = int((n % (i * 10) / i))
        k = k + 1
        i = i * 10
        print(rozryad)
# def func(n1, n2):
#     y = rozryady(n1) + rozryady(n2)
#     return str(y[5] + y[2]) + str(y[1] + y[4]) + str(y[0] + y[3])
#
# def suma_2(n1, n2, n3):
#     sum_x = func(n1, n2)
#     sum_y = func(n1, n3)
#     sum_z = func(n2, n3)
#     print(sum_x), print(sum_y), print(sum_z)

def int_input_array(m = " "):
    try:
        numbers = (input().split(" "))
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Enter 3 numbers with a space")
        return int_input_array(m)
    if (len(numbers) < 3):
        return int_input_array(m)
    return numbers
def main():
    print("Enter your numbers")
    n = int_input_array()
    # suma_1(n[0], n[1], n[2])
    print("-----------------")
    #suma_2(n[0], n[1], n[2])
    # print(rozryady(n[0]))
    # print(rozryady(n[1]))
    print(rozryady(n[2]))
    print(n)
main()