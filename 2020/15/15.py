
import time


def f1(fileName, turnLimit):
    f = open(fileName, 'r')
    nums = [int(n) for n in f.readline().split(',')]
    d = {nums[i]:[i+1] for i in range(len(nums))}

    turn = len(d) +1
    while turn <= turnLimit:
        last = nums[-1]
        if len(d[last]) == 1:
            nums.append(0)
            d[0].append(turn)
        else:
            diff = d[last][-1]-d[last][-2]
            nums.append(diff)
            if diff in d.keys():
                if len(d[diff]) > 1:
                    d[diff][0] = d[diff][1]
                    d[diff][1] = turn
                else:
                    d[diff].append(turn)
            else:
                d[diff] = [turn]
        turn += 1
    # for k in sorted(d.keys()):
    #     print(k,d[k])
    # print(nums)
    return nums[-1]







# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f, 2020)) # 203
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
# /!\ part 2 is very long
# start_time = time.time()
# print(f1(f, 3000000)) # 9007186
# print("--- %s seconds ---" % (time.time() - start_time))

