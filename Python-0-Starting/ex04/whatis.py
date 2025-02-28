import sys

def listlen(list):
    count = 0
    while list:
        count += 1
        list = list[count:]
    return count

ac = listlen(sys.argv[1:])

if ac == 1:
    av = sys.argv[1:][0]
    if not av.isdigit() and not av[1:].isdigit():
        print("AssertionError: argument is not an integer")
    else:
        if int(av) % 2:
            print("I am Odd")
        else:
            print("I am Even")
