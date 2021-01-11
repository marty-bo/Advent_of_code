
import time

# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(sum([int(int(n.split()[0])/3)-2 for n in open(f).readlines()]))
print("--- %s seconds ---" % (time.time() - start_time))


def count_fuel(quantity):
    tmp = int(quantity/3)-2
    if tmp>0:
        return tmp + count_fuel(tmp)
    else:
        return 0


# Part 2
start_time = time.time()
print(sum([count_fuel(int(n.split()[0])) for n in open(f).readlines()]))
print("--- %s seconds ---" % (time.time() - start_time))

