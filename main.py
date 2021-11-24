import random
import linkedlist


def start_metod():
    s = linkedlist.LinkedList()
    while True:
        print("\n Help Messenger:"
                    "\n1 - Generator massive; "
                    "\n2 - Iterator massive; "
                    "\n3 - Delete duplicate items;  "
                    "\n4 - Add element to 'k' position;  "
                    "\n5 - Delete element by 'k' position;  "
                    "\n6 - Exit. \n")
        try:
            n = int(input())
            if n == 1:
                num = enter_number()
                print("The array is entered ")
                make_by_generator(s, num)
                s.display()
            elif n == 2:
                num = enter_number()
                print("Random massive")
                make_by_iter(s, num),
                s.display()
            elif n == 3:
                s.remove_duplicates()
                print("Changed massive ")
                s.display()
            elif n == 4:
                while True:
                    try:
                        item = int(input("Enter elem \n"))
                        pos = int(input("Enter pos \n"))
                        break
                    except ValueError:
                        print('\nEnter elem')
                add_elem(s, item, pos)
                print("Changed massive ")
                s.display()
            elif n == 5:
                while True:
                    try:
                        pos = int(input("Enter pos to delete elem \n"))
                        break
                    except ValueError:
                        print('\nEnter number')
                del_elem(s, pos)
                print("Changed massive  ")
                s.display()
            elif n == 6:
                print("Exit")
                break
            else:
                continue
        except ValueError:
            print('\nEnter number')


def add_elem(a, item, pos):
    a.insert(item, pos)


def del_elem(a, pos):
    a.delete(pos)


def genrt(a, b):
    yield random.randint(a, b)


def make_by_generator(my_list, n):
    while True:
        try:
            a = int(input("Enter left border - а "))
            b = int(input("Enter right border - b "))
            if a > b:
                print("a should not be more than b \n")
                continue
            break
        except ValueError:
            print('\nEnter number')

    for i in range(n):
        my_list.append(linkedlist.Node(*genrt(a, b)))

    return my_list


def make_by_iter(my_list, n):
    while True:
        try:
            a = int(input("Enter left border - а "))
            b = int(input("Enter right border - b "))
            if a > b:
                print("a should not be more than b \n")
                continue
            break
        except ValueError:
            print('\nEnter number')

    for i in range(n):
        my_list.append(linkedlist.Node(random.randint(a, b)))

    return my_list


def enter_number():
    while True:
        try:
            n = int(input('Count of elem \n'))
            if n == 0:
                print('\nEnter number > 0 ')
                continue
            if n < 0:
                print('\nEnter number > 0 ')
                continue
            break
        except ValueError:
            print('\nEnter number')
    return n


if __name__ == '__main__':
    start_metod()
