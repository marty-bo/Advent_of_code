
import time

# import tkinter as tk


def f1():
    N = 1000
    
    map = [[0 for j in range(N)] for i in range(N)]

    f = open('input.txt')
    for line in f.readlines():
        line = [int(n) for n in line.replace('\n','').replace(' -> ',',').split(',')]
        line = [
            min(line[0], line[2]), 
            min(line[1], line[3]), 
            max(line[0], line[2]), 
            max(line[1], line[3])]
        if line[0] == line[2] or line[1] == line[3]:
            for i in range(line[1], line[3]+1):
                for j in range(line[0], line[2]+1):
                    map[i][j] += 1
    f.close()    

    count = 0
    for i in range(N):
        for j in range(N):
            count += map[i][j] > 1

    print('[f1]: Count = {}'.format(count))

    return


def f2():

    N = 1000

    # win = tk.Tk()
    # win.geometry("1000x1000")
    # canvas = tk.Canvas(win, width=1000, height=1000)
    # canvas.pack()
    
    map = [[0 for j in range(N)] for i in range(N)]

    f = open('input.txt')
    for line in f.readlines():
        line = [int(n) for n in line.replace('\n','').replace(' -> ',',').split(',')]
        # canvas.create_line(line[0], line[1], line[2], line[3])
        tx = 1 if line[0]<line[2] else (0 if line[0]==line[2] else -1)
        ty = 1 if line[1]<line[3] else (0 if line[1]==line[3] else -1)
        length = max(abs(line[0] - line[2]), abs(line[1] - line[3])) + 1
        for i in range(length):
            map[line[1] + ty*i][line[0] + tx*i] += 1
    f.close()    

    count = 0
    for i in range(N):
        for j in range(N):
            count += map[i][j] > 1

    print('[f2]: Count = {}'.format(count))

    # win.mainloop()
    return




print("########################################")
start_time = time.time()
f1()
print("--------- %.7s seconds ---------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("--------- %.7s seconds ---------" % (time.time() - start_time))

