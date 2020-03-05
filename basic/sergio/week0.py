def add(V, W):

    Z = []
    for v, w in zip(V, W):
        row = []
        for vv, ww in zip(v, w):
            row.append(vv + ww)
        Z.append(row)
    return Z


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
assert add(matrix1, matrix2) == [[3, -3], [-3, 3]]

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
assert add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]



# Bonus 1
def add(*args):
    # unpack args
    matrix = []
    for vects2sum in zip(*args):
        vector = []
        for elem2sum in zip(*vects2sum):
            vector.append(sum(elem2sum))
        matrix.append(vector)
    return matrix


matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
assert add(matrix1, matrix2, matrix3) == [[8, 8], [7, 7]]

# Bonus 2
# Bonus 2
def add(*args):
    # Check dimensions are correct
    try:
        if all([len(matrix) == len(args[0]) for matrix in args]) == False:
            raise ValueError
    except ValueError as v_error:
        print("Given matrices are not the same size.")
        return v_error

    for rows in zip(*args):
        l = []
        for row in rows:
            l.append(len(row))
        try:
            if all([x == l[0] for x in l]) == False:
                raise ValueError
        except ValueError as v_error:
            print("Given matrices are not the same size.")
            return v_error

    # Matrix Sum
    matrix = []
    for vects2sum in zip(*args):
        vector = []
        for elem2sum in zip(*vects2sum):
            vector.append(sum(elem2sum))
        matrix.append(vector)
    return matrix


assert isinstance(add([[1, 9], [7, 3]], [[1, 2], [3]]), ValueError) 

