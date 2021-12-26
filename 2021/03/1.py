
import time



def count_bit(list, bit_id):
    count = [0, 0]
    for e in list:
        count[e[bit_id] == '1'] += 1
    return count



def binary_to_decimal(binary):
    print('---',binary)
    res = 0
    for b in binary:
        res *= 2
        res += b == '1'
    print(res)
    return res



def f1():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    counts = []
    for i in range(12):
        counts.append(count_bit(lines, i))
        
    gamma = 0
    epsilon = 0
    for c in counts:
        gamma *= 2
        epsilon *= 2
        if c[0] > c[1]:
            gamma += 0
            epsilon += 1
        else:
            gamma += 1
            epsilon += 0

    print('[f1]:','\ngamma =',gamma,'\nepsilon =',epsilon,'\nepsilon*gamma =',epsilon*gamma,'\n')
    return



def f2():
    f = open('input.txt', 'r')
    lines = [l.replace('\n', '') for l in f.readlines()]
    f.close()

    # search the oxygen generator rating
    oxygen_list = lines.copy()
    for i in range(12):
        if len(oxygen_list) <= 1:
            break
        # find the most popular bit at index <i> in <oxygen_list>
        count = count_bit(oxygen_list, i)
        bit = '0' if count[0] > count[1] else '1'
        # remove all values that do not have the most popular bit
        for j in range(len(oxygen_list))[::-1]:
            if oxygen_list[j][i] != bit:
                oxygen_list.pop(j)
    if len(oxygen_list) != 1:
        print('[f2]: Error')
        return 0
    oxygen = binary_to_decimal(oxygen_list[0])

    # search the CO2 generator rating
    co2_list = lines.copy()
    for i in range(12):
        if len(co2_list) <= 1:
            break
        # find the most popular bit at index <i> in <co2_list>
        count = count_bit(co2_list, i)
        bit = '0' if count[0] <= count[1] else '1'
        # remove all values that do not have the most popular bit
        for j in range(len(co2_list))[::-1]:
            if co2_list[j][i] != bit:
                co2_list.pop(j)
    if len(co2_list) != 1:
        print('[f2]: Error')
        return 0
    co2 = binary_to_decimal(co2_list[0])
    
    print('[f2]: oxygen = {}\nCO2 = {}\noxygen*CO2 = {}\n'.format(oxygen, co2, oxygen*co2))
    return


print("------------------")
start_time = time.time()
f1()
print("--- %s seconds ---" % (time.time() - start_time))


print("------------------")
start_time = time.time()
f2()
print("--- %s seconds ---" % (time.time() - start_time))
