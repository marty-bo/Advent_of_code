
import time

def f1():
    res = 0
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            res += 1
    print("f1:",res)
    return res


def f2():
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    win = 0
    for i in range(3):
        win += nums[i]
    old_win = win
    res = 0
    for i in range(3, len(nums)):
        win -= nums[i-3]
        win += nums[i]
        if win > old_win:
            res += 1
        old_win = win
    print("f2:",res)
    return res





print("------------------")
start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))

print("------------------")
start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))
