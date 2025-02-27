def NULL_not_found(object: any) -> int:
    
    if not object or object == 'nan':
        print(f"{object} {type(object)}")
        return 0 
    print("Type not Found$")   
    return 1


