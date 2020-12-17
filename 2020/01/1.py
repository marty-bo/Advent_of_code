
import time

def f1():
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    l = [0]*2020
    for i in nums:
        l[i] = i
    for i in nums:
        if l[2020-i] != 0:
            print(i * (2020-i))
            f.close()
            return None
    f.close()
    return None


def f1_2():
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == 2020:
                print(nums[i]*nums[j])
                f.close()
                return None
    f.close()
    return None
    
def f2():
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    l = [0]*4040
    for i in nums:
        l[i] = i
    for i in nums:
        for j in range(0, 2020-i+1):
            if l[j] == 0:
                continue
            if l[j] + i > 2020:
                continue
            if l[2020-(i+l[j])] != 0:
                print((2020-(i+l[j])) * l[j] * i)
                f.close()
                return None
    f.close()
    return None


def f2_2():
    f = open('input.txt', 'r')
    nums = [ int(l) for l in f.readlines()]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 2020:
                    print(nums[i]*nums[j]*nums[k])
                    f.close()
                    return None
    f.close()
    return None
    


start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
f1_2()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
f2_2()
print("--- %s seconds ---" % (time.time() - start_time))