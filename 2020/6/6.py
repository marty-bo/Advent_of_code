
import time





def f1():
    f = open('input.txt', 'r')
    answers = {}
    for l in 'abcdefghijklmnopqrstuvwxyz':
        answers[l] = 0
    count = 0
    for line in f.readlines():
        if line.split() == []:
            for l in answers.keys():
                count += answers[l]
                answers[l] = 0
            #print(count)
            continue
        for l in line.split():
            for c in l:
                answers[c] = 1
        #print(answers)

    for l in answers.keys():
        count += answers[l]
        answers[l] = 0
    f.close()
    return count


def f2():
    f = open('input.txt', 'r')
    answers = {}
    for l in 'abcdefghijklmnopqrstuvwxyz':
        answers[l] = 0
    count = 0
    nbPerson = 0
    for line in f.readlines():
        if line.split() == []:
            for l in answers.keys():
                if answers[l]==nbPerson:
                    count += 1
                answers[l] = 0
            nbPerson = 0
            # print(count)
            continue

        for l in line.split():
            for c in l:
                answers[c] += 1
            nbPerson += 1
        #print(answers)

    for l in answers.keys():
        if answers[l]==nbPerson:
            count += 1
    f.close()
    return count




# ####### MAIN #######

# Part 1
start_time = time.time()
print(f1())
print("--- %s seconds ---" % (time.time() - start_time))
# Part 2
start_time = time.time()
print(f2())
print("--- %s seconds ---" % (time.time() - start_time))
