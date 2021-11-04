def int_arr():
    i = 0
    arr = []
    n = check_2()
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
        return check_1()
    return x
def check_2():
    n = check_1()
    if n <= 0:
        print("Number must be > 0 ")
        return check_2()
    return n
def main():
    arr = int_arr()
    print(arr)
    print("----------")
    print(sort(arr))
main()