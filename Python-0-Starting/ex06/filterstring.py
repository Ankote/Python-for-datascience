import sys


def ac():
    """
    Counts the number of command-line arguments\
    provided (excluding the script name).

    Returns:
        int: The number of command-line arguments.
    """
    return len(sys.argv[1:])


def av():
    """
    Retrieves the command-line arguments\
    provided to the script (excluding the script name).

    Returns:
        list: A list of command-line arguments.
    """
    return sys.argv[1:]


def main(ac, av):
    if ac != 2 or not av[1].isdigit():
        print("AssertionError: the arguments are bad")
        return
    list = []
    cpt = 0
    str = av[0]
    for char in av[0]:
        if not char.isalpha():
            if char != ' ':
                print("AssertionError: the arguments are bad")
                list.clear()
                return
            else:
                if cpt > int(av[1]):
                    list.append(str[:cpt])
                str = str[cpt + 1:]
                cpt = 0
        cpt += 1
    if cpt - 1 > int(av[1]):
        list.append(str[:cpt - 1])
    print(list)
    list.clear()
    return


if __name__ == "__main__":
    main(ac(), av())
