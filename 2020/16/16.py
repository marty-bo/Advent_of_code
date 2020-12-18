
import time


def f1(fileName):
    f = open(fileName, 'r')
    nums = []
    # rules
    while 1:
        l = f.readline()
        if l.split() == []:
            break
        nums.append([[int(i) for i in l.split(':')[1].split()[0].split('-')], [int(i) for i in l.split(':')[1].split()[2].split('-')]])

    # 'your ticket:'
    f.readline()
    # your ticket values
    your_ticket = [int(i) for i in f.readline().split()[0].split(',')]

    # '\n'
    f.readline()

    # 'nearby tickets:'
    f.readline()
    # nearby tickets values
    invalid = []
    while 1:
        l = f.readline().split()
        if l == []:
            break
        ticket = [int(i) for i in l[0].split(',')]
        for v in ticket:
            valid = False
            for [[rmin1, rmax1], [rmin2, rmax2]] in nums:
                if (v >= rmin1 and v <= rmax1) or (v >= rmin2 and v <= rmax2):
                    valid = True
                    break
            if not valid:
                invalid.append(v)
    return sum(invalid)

            




# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

