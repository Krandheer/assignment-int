def square_root(x):
    """return sqrt if int or floor value of square root"""
    if x in [0, 1]:
        return x
    if x < 4:
        return 1
    for j in range(x // 2, 1, -1):
        if j * j <= x:
            return j


# temp = [2, 3, 4, 5, 6, 8, 9]
# for i in temp:
#     print(square_root(i))
