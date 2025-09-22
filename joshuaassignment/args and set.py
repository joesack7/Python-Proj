def merge_lists(*lists):
    final = []
    for num in lists:
        for item in num:
            if item not in final:
                final.append(item)
    return final
