def suma_1(n1, n2, n3):
    sum_1 = n1 + n2
    sum_2 = n1 + n3
    sum_3 = n2 + n3
    print(sum_1, sum_2, sum_3, sep="\n")

def rozryady(n):
    if n > 999:
        print("Your number is huge")
        int_input_array()
    rozryad_1 = n % 10
    rozryad_2 = int((n % 100) / 10)
    rozryad_3 = int((n % 1000) / 100)
    return rozryad_1, rozryad_2, rozryad_3

def func(n1, n2):
    y = rozryady(n1) + rozryady(n2)
    return str(y[5] + y[2]) + str(y[1] + y[4]) + str(y[0] + y[3])

def suma_2(n1, n2, n3):
    sum_x = func(n1, n2)
    sum_y = func(n1, n3)
    sum_z = func(n2, n3)
    print(sum_x), print(sum_y), print(sum_z)

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
    suma_1(n[0], n[1], n[2])
    print("-----------------")
    suma_2(n[0], n[1], n[2])
main()