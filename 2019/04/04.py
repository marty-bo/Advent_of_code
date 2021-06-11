
import time



FILE1 = "input_1.txt"

# check if val is valid
def validation_part1(val):
    double = False
    prev = -1
    for i in range(len(val)):
        if val[i] == prev:
            double = True
        elif val[i] < prev:
            return False
        prev = val[i]
    return double


# check if val is valid
def validation_part2(val):
    double = False
    tmpDouble = False
    state = 0
    prev = -1
    for i in range(len(val)):
        if val[i] == prev:
            if state == 0:
                tmpDouble = True
                state = 1
            elif state == 1:
                tmpDouble = False
                state = 2
        elif val[i] < prev:
            return False
        else:
            if state == 1:
                double = True
            state = 0
        prev = val[i]

    if state == 1:
        double = True
    return double


# return True is valMin is less than valMax, False otherwise
def inferior(valMin, valMax):
    for i in range(len(valMin)):
        if valMin[i] < valMax[i]:
            return True
        if valMin[i] == valMax[i]:
            continue
        if valMin[i] > valMax[i]:
            return False
    # equals
    return False

# return False if overflow, True otherwise
def increment(val):
    i = len(val)-1
    while True:
        if i < 0:
            return False
        val[i] += 1
        if val[i] > 9:
            val[i] = 0
            i -= 1
        else:
            break
    return True


def f1(valMin, valMax):
    count = 0
    while inferior(valMin, valMax):
        if not increment(valMin):
            print("Overflow")
            return
        if validation_part1(valMin):
            count += 1
    return count

      
def f2(valMin, valMax):
    count = 0
    while inferior(valMin, valMax):
        if not increment(valMin):
            print("Overflow")
            return
        if validation_part2(valMin):
            count += 1
    return count  



def main(filename1):
    start_time = time.time()
    print(f1(*[[int(c) for c in list(v)] for v in open(filename1).readline().split("-")]))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(f2(*[[int(c) for c in list(v)] for v in open(filename1).readline().split("-")]))
    print("--- %s seconds ---" % (time.time() - start_time))

main(FILE1)