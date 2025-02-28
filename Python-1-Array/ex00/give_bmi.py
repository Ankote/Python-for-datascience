def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """function take 2 lists of integers or floats\
 in input and returns a list
of BMI values.
    """
    lisrRes = []
    if len(height) != len(weight):
        print('AssertionError : Lists sixe not match')
        return []

    for i, item in enumerate(height, 0):
        if not isinstance(item, (int, float))\
                or weight[i] < 0 or not isinstance(weight[i], (int, float))\
                or item < 0:
            lisrRes.clear()
            print('AssertionError : (hint) List have \
to be in same size and contain only \
intigers or floats')
            return []
        # Given height in cm and weight in kg
        height_m = item
        weight_kg = weight[i]
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        lisrRes.append(round(bmi, 2))
    return lisrRes


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for item in bmi:
        if not isinstance(item, (int, float)):
            print('AssertionError : (hint) List have \
to be in same size and contain only \
intigers or floats')
            return None
        if item > limit:
            res.append(True)
        else:
            res.append(False)
    return res


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
