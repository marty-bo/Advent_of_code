
import time

# import tkinter as tk


def f1(days):

    # read input
    f = open('input.txt')
    # number of fish with a timer at <i> (key)
    lanternfishes = {i:0 for i in range(9)}
    for num in f.readline().split(','):
        lanternfishes[int(num)] += 1
    f.close() 

    for day in range(days):
        tmp_lanternfishes = {i:0 for i in range(9)}
        # if timer is equal to 0
        tmp_lanternfishes[8] += lanternfishes[0]
        tmp_lanternfishes[6] += lanternfishes[0]
        # if timer is greater than 0
        for i in range(1, 9):
            tmp_lanternfishes[i-1] += lanternfishes[i]
        lanternfishes = tmp_lanternfishes

    print('[f]: Days = {} Total = {} Lanternfishes = {}'.format(days, sum(lanternfishes.values()),lanternfishes))


    return



print("########################################")
start_time = time.time()
f1(days=80)
print("--------- %.7s seconds ---------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f1(days=256)
print("--------- %.7s seconds ---------" % (time.time() - start_time))
