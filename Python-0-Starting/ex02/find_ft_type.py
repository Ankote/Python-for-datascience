def all_thing_is_obj(object: any) -> int:

    if (type(object) == type("hello")):
        print(f"{object} is in the kitchen");
    elif not type(object):
        print("Type not found$")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return 42
