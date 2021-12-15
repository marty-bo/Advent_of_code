
import time

def f1():

    left_cost = 0
    left_count = 0
    right_cost = 0
    right_count = 0
    current_pos = 0
    best_pos = 0
    best_pos_cost = 0
    max_pos = 0

    # read input
    f = open('input.txt')
    horizontals = dict()
    for num in f.readline().split(','):
        num = int(num)
        if horizontals.get(num) != None:
            horizontals[num] += 1
        else :
            horizontals[num] = 1
        if num != 0:
            right_count += 1
            right_cost += num
        if num > max_pos:
            max_pos = num
    f.close() 
    best_pos_cost = right_cost

    for i in range(max_pos+1):
        left_cost += horizontals.get(current_pos, 0) + left_count
        left_count += horizontals.get(current_pos, 0)
        current_pos += 1
        right_cost -= right_count
        right_count -= horizontals.get(current_pos, 0)
        current_cost = left_cost + right_cost
        if current_cost <= best_pos_cost:
            best_pos_cost = current_cost
            best_pos = current_pos
        
    print('[f1]: best_pos = %7d best_pos_cost = %7d' % (best_pos, best_pos_cost))
    return


def f2():

    def cost(dist):
        # cost(n) = n + cost(n-1)
        return int((dist * (dist+1)) / 2)
    
    left_cost = 0
    left_count = 0
    left_one_step_cost = 0

    right_cost = 0
    right_count = 0
    right_one_step_cost = 0

    current_pos = 0
    current_cost = 0

    best_pos = 0
    best_pos_cost = 0

    max_pos = 0

    # read input and init
    f = open('input.txt')
    horizontals = dict()
    for num in f.readline().split(','):
        num = int(num)

        if horizontals.get(num) != None:
            horizontals[num] += 1
        else :
            horizontals[num] = 1

        if num != 0:
            right_count += 1
            right_cost += cost(num)
            right_one_step_cost += num

        if num > max_pos:
            max_pos = num
    f.close() 
    current_cost = right_cost
    best_pos_cost = current_cost

    for i in range(max_pos+1):
        left_count += horizontals.get(current_pos, 0)
        left_one_step_cost += left_count
        left_cost += left_one_step_cost
        current_pos += 1
        right_cost -= right_one_step_cost
        right_one_step_cost -= right_count
        right_count -= horizontals.get(current_pos, 0)
        current_cost = left_cost + right_cost
        if current_cost <= best_pos_cost:
            best_pos_cost = current_cost
            best_pos = current_pos
        
    print('[f2]: best_pos = %7d best_pos_cost = %7d' % (best_pos, best_pos_cost))
    return


print("########################################")
start_time = time.time()
f1()
print("--------- %.7s seconds ---------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f2()
print("--------- %.7s seconds ---------" % (time.time() - start_time))
