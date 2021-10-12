def rozryady(n):
    i = 1
    k = 0
    arr = []
    while k < len(str(n)):
        rozryad = int((n % (i * 10) / i))
        k = k + 1
        i = i * 10
        arr.append(rozryad)
    return arr
def sum(n1, n2):
    sum = []
    for m1, m2 in zip(n1, n2):
        sum.insert(0, m1+m2)
    if len(n1) < len(n2):
        n2, n1 = n1, n2
    for x in n1[len(n2):]:
        sum.insert(0, x)
    return sum



def convert_array(array, sep = ""):
    str1 = sep
    return (str1.join(str(s) for s in array))

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
    mas = []
    result = []
    for i in n:
        mas.append(rozryady(i))
    i = 0
    j = 1
    while i < 3:
        while j < 3:
            print(convert_array(sum(mas[i], mas[j])))
            j = j + 1
        i = i + 1
        j = 0
main()
