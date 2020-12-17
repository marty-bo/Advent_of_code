
import time








def f1():
    f = open('input.txt', 'r')
    maxId = 0
    for line in f.readlines():
        h_max = 127
        h_min = 0
        v_min = 0
        v_max = 7
        for c in line[:7]:
            if c == 'F':
                h_max -= (h_max+1-h_min)>>1
            else:
                h_min += (h_max+1-h_min)>>1
        for c in line[7:]:
            if c == 'L':
                v_max -= (v_max+1-v_min)>>1
            else:
                v_min += (v_max+1-v_min)>>1
        maxId=max(maxId, h_min*8+v_min)
        #print(h_min, v_min, h_min*8+v_min)

    f.close()
    return maxId


def f2():
    f = open('input.txt', 'r')
    maxId = 0
    seats = []
    for i in range(128):
        seats.append([])
        for j in range(8):
            seats[i].append(0)
    for line in f.readlines():
        h_max = 127
        h_min = 0
        v_min = 0
        v_max = 7
        for c in line[:7]:
            if c == 'F':
                h_max -= (h_max+1-h_min)>>1
            else:
                h_min += (h_max+1-h_min)>>1
        for c in line[7:]:
            if c == 'L':
                v_max -= (v_max+1-v_min)>>1
            else:
                v_min += (v_max+1-v_min)>>1
        seats[h_min][v_min]=1
        maxId=max(maxId, h_min*8+v_min)
        #print(h_min, v_min, h_min*8+v_min)
  #for r in seats:
       # print(r)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if i>0 and seats[i][j]==0 and seats[i-1][j]==1 and seats[i+1][j]==1:
                print(i,j)
                f.close()
                return i*8+j
    f.close()
    return -1





# ####### MAIN #######

# Part 1
start_time = time.time()
print(f1())
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2())
print("--- %s seconds ---" % (time.time() - start_time))
