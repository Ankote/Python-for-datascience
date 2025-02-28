import sys


def ac():
    """
    Counts the number of command-line\
    arguments provided (excluding the script name).

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
    """
     encodes Provide string into Morse Code.
    Args:
        ac (int): The number of command-line arguments.
        av (list): The list of command-line arguments.
    The program supports space and alphanumeric characters
    • An alphanumeric character is represented by dots . and dashes -
    • Complete morse characters are separated by a single space
    • A space character is represented by a slash /
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        ".": ".-.-.- ",
        ",": "--..-- ",
        "?": "..--.. ",
        "!": "-.-.-- ",
        "'": ".----. ",
        "-": "-....- ",
        "/": "-..-. ",
    }
    morse_text = ''

    if ac != 1:
        print("AssertionError: the arguments are bad")
        return
    for char in av[0]:
        if char.upper() not in NESTED_MORSE.keys():
            print("AssertionError: the arguments are bad")
            return
        else:
            morse_text += NESTED_MORSE[char.upper()]
    print(morse_text)
    return


if __name__ == "__main__":
    main(ac(), av())
