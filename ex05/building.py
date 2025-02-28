import sys


def ac():
    count = 0
    args = sys.argv[1:]
    while args:
        count += 1
        args = args[count:]
    return count


def av():
    return sys.argv[1:]


def main(ac, av):
    str = ''
    lowerCount = 0
    upperCount = 0

    if ac > 1:
        print('AssertionError : invalid number of args')
        return
    if ac < 1:
        str = input("Enter text :  ")
    elif ac == 1:
        str = av[0]
    for char in str:
        if char.isupper():
            upperCount += 1
        if char.islower():
            lowerCount += 1
    print(f"{upperCount} upper letters")
    print(f"{lowerCount} lower letters")
    return


if __name__ == "__main__":
    main(ac(), av())
