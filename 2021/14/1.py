
import time

def f(steps):

    f = open('input.txt')


    # read template
    template = f.readline().replace('\n','')
    f.readline()

    # store the first and the last letter of the template
    # # useful to count the number of letter at the end
    first_letter = template[0]
    last_letter = template[-1]

    # store the number of pair
    pair_counts = dict()

    # read pair insertion rules
    pair_insertion_rules = dict()
    for line in f.readlines():
        line = line.replace('\n', '').split(' -> ')
        pair_insertion_rules[line[0]] = line[1]
        # init all pair at 0
        pair_counts[line[0]] = 0
    f.close()

    # count the number of pair in template (init)
    # example: ABCBC -> {'AB':1, 'BC':2, 'CB':1}
    for i in range(len(template)-1):
        pair_counts[template[i]+template[i+1]] += 1

    # apply rules for the given number of steps 
    for step in range(steps):
        tmp_pair_counts = dict(zip(pair_counts.keys(), [0 for i in range(len(pair_counts.values()))]))
        for (key, val) in zip(pair_counts.keys(), pair_counts.values()):
            # if key=AB val=10 and pair_insertion_rules[AB]=C
            # tmp_pair_counts[AC] += 10
            tmp_pair_counts[key[0] + pair_insertion_rules[key]] += val
            # tmp_pair_counts[CB] += 10
            tmp_pair_counts[pair_insertion_rules[key] + key[1]] += val
        pair_counts = tmp_pair_counts
    # print(pair_counts)

    # count the number of letters
    letters = set()
    for key in pair_counts.keys():
        letters.add(key[0])
        letters.add(key[1])
    letter_count = dict(zip(letters, [0 for i in range(len(letters))]))
    for (key, val) in zip(pair_counts.keys(), pair_counts.values()):
        letter_count[key[0]] += val
        letter_count[key[1]] += val
    # add one occurence of the first and the last letter
    letter_count[first_letter] += 1
    letter_count[last_letter] += 1
    # divide the count by 2 because:
    # ABC -> {'AB':1, 'BC':1} -> B appears 1+1 times in the dict
    for key in letter_count.keys():
        letter_count[key] /= 2
    # print(letter_count)

    print('[f]: Res = %d' % (max(letter_count.values()) - min(letter_count.values())))

    return 0
    



print("########################################")
start_time = time.time()
f(10)
print("----------- %.8s seconds -----------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f(40)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
