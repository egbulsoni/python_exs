def are_true(a, b):
    if a and b:
        return "both"
    if not a and not b:
        return "neither"
    return "first" if a else "second"
