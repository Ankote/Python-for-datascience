def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        print("ERROR:  slice_me(->family: list<-, start: int, end: int)")
        return None
    if not isinstance(start, int):
        print("ERROR:  slice_me(family: list, ->start: int<-, end: int)")
        return None
    if not isinstance(end, int):
        print("ERROR:  slice_me(family: list, start: int, ->end: int<-)")
        return None
    nestedListLen = len(family[0])
    for item in family:
        if not isinstance(item, list) or len(item) != nestedListLen:
            print("ERROR: All elements of family\
must be lists of the same length.")
            return None
    sliced_family = family[start:end]
    if not sliced_family:  # Handling out-of-range slicing
        print("ERROR: Slice is out of range, returning empty list.")
        return []
    print(f"My shape is : {len(family), nestedListLen}")
    print(f"My new shape is : ({len(sliced_family)}, {len(sliced_family[0])})")
    return sliced_family


def main():
    family = [
        [1.80, 78.4], [2.15, 102.7],
        [2.10, 98.5], [1.88, 75.2]
    ]
    print(slice_me(family, -44, 4))  # Out-of-range example


if __name__ == "__main__":
    main()
