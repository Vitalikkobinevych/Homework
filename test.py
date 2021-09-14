print("Enter number of element ")
try:
    n = int(input())
except ValueError:
    print("Invalid value")
i = 0
arr = []
while i < n:
    print("Enter number ")
    try:
        x = int(input())
    except ValueError:
        print("Invalid value")
    arr.append(x)
    i = i + 1
print(arr)
print("----------")
arr = list(set(arr))
print(arr)
