import time

from Configuration import string_to_config
from Solver import Solver


def read_input(filename):
    f = open('input.txt')
    config = string_to_config([line.replace('\n','') for line in f.readlines()], 0)
    f.close()
    return config


def f1():

    config = read_input('input.txt')

    solver = Solver()
    cost = solver.solve(config)

    print('[f1]: Least energy required = %d' % (cost))

    return



print("########################################")
start_time = time.time()
f1()
print("----------- %.8s seconds -----------" % (time.time() - start_time))
