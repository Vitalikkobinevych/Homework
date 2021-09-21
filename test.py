def int_arr():
    i = 0
    arr = []
    while i < n:
        print("Enter number ")
        x = check_1()
        arr.append(x)
        i = i + 1
    return arr
def sort(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr
def check_1():
    try:
        x = int(input())
    except ValueError:
        print("Invalid value")
        print("Must be number ")
        check_1()
    return x
def check_2():
    try:
        n = int(input("Enter number of element "))
    except ValueError:
        print("Invalid value")
        check_2()
    if n <= 0:
        print("Number must be > 0 ")
        check_2()
    return n
n = check_2()
arr = int_arr()
print(arr)
print("----------")
print(sort(arr))