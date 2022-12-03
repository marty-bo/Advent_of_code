
import time
import os

input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

def count_calories_per_elves(str_arr: list[str]) -> list:
    """ return the amount of calories carried by each elve """
    calories = []
    current = 0
    for line in str_arr:
        if line == '':
            calories.append(current)
            current = 0
        else:
            current += int(line)
    return calories

def get_n_max_values_of_arr(arr: list[int], n: int):
    return sorted(arr, reverse=True)[:n]

def f1():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()
    calories = count_calories_per_elves(map(lambda line: line.replace('\n', ''), lines))
    print("Maximum calories carried is %d" % max(calories))
    return

def f2():
    f = open(input_file_path)
    lines = f.readlines()
    n = 3
    f.close()
    calories = count_calories_per_elves(map(lambda line: line.replace('\n', ''), lines))
    count_n = sum(get_n_max_values_of_arr(calories, n))
    print("Sum of %d most carried calories is %d" % (n, count_n))
    return


print("Begin task 1...")
start_time = time.time()
f1()
print("End task 1 in  %.8s seconds." % (time.time() - start_time))


print("Begin task 2...")
start_time = time.time()
f2()
print("End task 2 in  %.8s seconds." % (time.time() - start_time))
