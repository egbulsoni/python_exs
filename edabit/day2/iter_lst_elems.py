def count_characters(lst):
    if not lst:
        return 0
    total = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            total += 1

    return total
