def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(intersection([4, 3, 2], [4, 2, 0]))