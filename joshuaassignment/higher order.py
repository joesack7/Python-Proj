def apply_operation(lst, operation):
    if operation == "square":
        return [num * num for num in lst]
    if operation == "double":
        return [num*num for num in lst]
    if operation == "negate":
        return [-num for num in lst]