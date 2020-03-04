# Base
def add(V, W):

    Z = []
    for v, w in zip(V, W):
        row = []
        for vv, ww in zip(v, w):
            row.append(vv + ww)
        Z.append(row)
    return Z


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[70, 80, 90], [40, 50, 60], [10, 20, 30]]
print(add(V=m1, W=m2))



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


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[10, 20, 30],
      [40, 50, 60],
      [70, 80, 90]]

m3 = [[100, 200, 300],
      [400, 500, 600],
      [700, 800, 900]]

print(add(m1, m2, m3, m1, m2, m3))

# Bonus 2


