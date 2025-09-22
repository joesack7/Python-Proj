def group_by_category(items):
    result = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        if category not in result:
            result[category] = []
        result[category].append(name)
    return result
