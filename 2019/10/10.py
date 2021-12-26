
import time


# return False if an asteroid is between a1 and a2
def canSee(a1, a2, asteroids):
    if a1[0]==a2[0] and a1[1]==a2[1]:
        return False
    offW = a1[0]
    offH = a1[1]
    for a in asteroids:
        # if same X axis
        if a1[0]==a2[0] and a1[0]==a[0]:
            if (a1[1]<a[1] and a[1]<a2[1]) or (a2[1]<a[1] and a[1]<a1[1]):
                return False
        # if same Y axis
        elif a1[1]==a2[1] and a1[1]==a[1]:
            if (a1[0]<a[0] and a[0]<a2[0]) or (a2[0]<a[0] and a[0]<a1[0]):
                return False
        # if 2 asteroids has the same axis but not the third
        elif (a1[0]==a2[0] or a2[0]==a[0] or a[0]==a1[0]) or (a1[1]==a2[1] or a2[1]==a[1] or a[1]==a1[1]):
            continue
        else:
            # if a is between a1 and a2
            if ((a1[0]<a[0] and a[0]<a2[0]) or (a2[0]<a[0] and a[0]<a1[0])) and ((a1[1]<a[1] and a[1]<a2[1]) or (a2[1]<a[1] and a[1]<a1[1])):
                if ((a2[0]-offW)/(a2[1]-offH)) == ((a[0]-offW)/(a[1]-offH)):
                    return False
    return True
        
            




def f1(filename):
    map = [[c for c in l.replace('\n','')] for l in open(filename).readlines()]
    print(*map,sep='\n')
    W = len(map[0])
    H = len(map)
    asteroids = []
    # for each asteroid in the map
    for h in range(H):
        for w in range(W):
            if map[h][w] == '.':
                continue
            asteroids.append([w,h,0])
    for i in range(len(asteroids)):
        for j in range(i+1, len(asteroids)):
            if canSee(asteroids[i], asteroids[j], asteroids):
                asteroids[i][2] += 1
                asteroids[j][2] += 1
    best = asteroids[0]
    for a in asteroids:
        if a[2] > best[2]:
            best = a
    return best
    

# Part 1
f = 'input_1.txt'
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))


