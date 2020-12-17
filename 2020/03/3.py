
import time



def f1(right, down):
    f = open('input.txt', 'r')
    trees = 0
    pos = right
    for i in range(down):
        length = len(f.readline().split()[0])
    for line in f.readlines()[::down]:
        if line[pos]=='#':
            trees += 1
        pos += right
        if pos >= length:
            pos %= length
        
    f.close()
    return trees




start_time = time.time()
print(f1(3,1))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(f1(1,1)*f1(3,1) * f1(5,1) * f1(7,1) * f1(1,2))
print("--- %s seconds ---" % (time.time() - start_time))
