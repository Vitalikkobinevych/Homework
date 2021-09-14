print ("Enter your numbers")
try:
    number_1, number_2, number_3 = (input().split(" "))
except ValueError:
    print("Invalid value")
def rozryad_1(x):
    return x % 10
def rozryad_2(y):
    return int((y % 100) / 10)
def rozryad_3(z):
    return int((z % 1000) / 100)
result_1 = str(rozryad_3(int(number_1)) + rozryad_3(int(number_2))) + str(rozryad_2(int(number_1)) + rozryad_2(int(number_2))) + str(rozryad_1(int(number_1)) + rozryad_1(int(number_2)))
result_2 = str(rozryad_3(int(number_1)) + rozryad_3(int(number_3))) + str(rozryad_2(int(number_1)) + rozryad_2(int(number_3))) + str(rozryad_1(int(number_1)) + rozryad_1(int(number_3)))
result_3 = str(rozryad_3(int(number_2)) + rozryad_3(int(number_3))) + str(rozryad_2(int(number_2)) + rozryad_2(int(number_3))) + str(rozryad_1(int(number_2)) + rozryad_1(int(number_3)))
if int(number_1) >=1 and int(number_1) <= 106:
    if int(number_2) >= 1 and int(number_2) <= 106:
        if int(number_3) >= 1 and int(number_3) <= 106:
            print(result_1)
            print(result_2)
            print(result_3)
        else:
            print("Wrong numbers")
    else:
        print("Wrong numbers")
else:
    print("Wrong numbers")