from collections import Counter
def most_frequent(lst):
    c = Counter(lst)
    return c.most_common(1)[0][0]
print(most_frequent([3, 3, 2, 4, 4, 1, 3, 3]))