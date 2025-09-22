def second_largest(data):
    if len(data)<2:
        return None
    large_number = second = float('-inf')
    for number in data:
        if number > large_number:
            second = large_number
            large_number = number
        elif number > second and number != large_number:
            second = number

    if second != float('-inf'):
        return second
    else:
        None