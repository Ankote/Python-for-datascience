import sys


def ac():
    """
    Counts the number of command-line arguments provided (excluding the script name).

    Returns:
        int: The number of command-line arguments.
    """
    return len(sys.argv[1:])


def av():
    """
    Retrieves the command-line arguments provided to the script (excluding the script name).

    Returns:
        list: A list of command-line arguments.
    """
    return sys.argv[1:]


def main(ac, av):
    """
    Counts and prints the number of uppercase and lowercase letters in the provided input.

    Args:
        ac (int): The number of command-line arguments.
        av (list): The list of command-line arguments.

    If one argument is provided via the command line, it processes that.
    If no argument is provided, it prompts the user for input.
    If more than one argument is provided, it prints an error message.
    """
    str = ''
    lowerCount = 0
    upperCount = 0

    if ac > 1:
        print('AssertionError : invalid number of args')
        return
    if ac < 1:
        try:
            str = input("Enter text :  ")
        except:
            print("")
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
