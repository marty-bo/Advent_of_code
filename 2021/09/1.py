
import time

def search_low_points(mat):
    low_points = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            low = True
            center = mat[i][j]
            for (ii,jj) in [(-1,0),(0,1),(1,0),(0,-1)]:
                if i+ii < 0 or i+ii >= len(mat):
                    continue
                if j+jj < 0 or j+jj >= len(mat[i+ii]):
                    continue
                if mat[i+ii][j+jj] <= center:
                    low = False
                    break
            if low == True:
                low_points.append((i, j))
    return low_points

def search_basins_size(mat, low_points):
    TMP_MAT = [[[height, False] for height in line] for line in mat]
    basins_size = []
    for point in low_points:
        basins_size.append(search_basins_size_rec(TMP_MAT, point))
    return basins_size

def search_basins_size_rec(mat, point):
    if point[0] < 0 or point[0] >= len(mat) or point[1] < 0 or point[1] >= len(mat[point[0]]):
        return 0
    if mat[point[0]][point[1]][0] == 9 or mat[point[0]][point[1]][1] == True:
        return 0
    mat[point[0]][point[1]][1] = True
    c = 1
    c += search_basins_size_rec(mat, [point[0]-1, point[1]])
    c += search_basins_size_rec(mat, [point[0], point[1]+1])
    c += search_basins_size_rec(mat, [point[0]+1, point[1]])
    c += search_basins_size_rec(mat, [point[0], point[1]-1])
    return c

def f1():
    count = 0
    f = open('input.txt')
    mat = [[int(height) for height in line.replace('\n','')] for line in f.readlines()]
    low_points = search_low_points(mat)
    for (i,j) in low_points:
        count += 1 + mat[i][j]
    print('[f2]: Count = %d' % (count))
    return
    

def f2():
    count = 0
    f = open('input.txt')
    mat = [[int(height) for height in line.replace('\n','')] for line in f.readlines()]
    low_points = search_low_points(mat)
    basins_size = search_basins_size(mat, low_points)
    basins_size = sorted(basins_size, reverse=True)
    count = basins_size[0] * basins_size[1] * basins_size[2]
    print('[f1]: Count = %d' % (count))
    return



print("########################################")
start_time = time.time()
f1()
print("--------- %.7s seconds ---------" % (time.time() - start_time))



print("########################################")
start_time = time.time()
f2()
print("--------- %.7s seconds ---------" % (time.time() - start_time))

