
import time
import os
import re

input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")


def get_overlap_sections(left_from: int, left_to: int, right_from: int, right_to: int) -> None | tuple[int, int]:
    if (left_from <= right_to and left_to >= right_from) or (right_from <= left_to and right_to >= left_from):
        return (max(left_from, right_from), min(left_to, right_to))
    return 0

def is_overlapping(left_from: int, left_to: int, right_from: int, right_to: int) -> bool:
    if (left_from <= right_to and left_to >= right_from) or (right_from <= left_to and right_to >= left_from):
        return True
    return False

def fully_contains(left_from: int, left_to: int, right_from: int, right_to: int) -> bool:
    if left_from <= right_from and left_to >= right_to:
        return True
    if right_from <= left_from and right_to >= left_to:
        return True
    return False

def f1():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()

    overlap_sum = 0
    for line in lines:
        numbers = re.findall(r"\d+", line)
        numbers = list(map(lambda n: int(n), numbers))
        overlap_sum += 1 if fully_contains(*numbers) else 0
    print("Total overlap is %d" % overlap_sum)
    return

def f2():
    f = open(input_file_path)
    lines = f.readlines()
    f.close()

    count_overlaping_sections = 0
    for line in lines:
        numbers = re.findall(r"\d+", line)
        numbers = list(map(lambda n: int(n), numbers))
        count_overlaping_sections += 1 if is_overlapping(*numbers) else 0

    print("Total overlap is %d" % count_overlaping_sections)
    return


print("Begin task 1...")
start_time = time.time()
f1()
print("End task 1 in  %.8s seconds." % (time.time() - start_time))

print("Begin task 2...")
start_time = time.time()
f2()
print("End task 2 in  %.8s seconds." % (time.time() - start_time))
