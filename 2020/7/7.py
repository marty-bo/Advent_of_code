
import time
import re



def f1():
    f = open('input.txt', 'r')
    D = {}
    for line in f.readlines():
        match = re.match(r'(.*) bags contain (?:no other bags.|(.*)[.])', line)
        #print('\n',match.groups())
        B = match[1]
        D[B] = []
        if match[2]:
            bag_list = match[2].split(', ')
            for bag in bag_list:
                match = re.match(r'\d+ ([a-zA-Z]* [a-zA-Z]*) bags?', bag)
                D[B].append(match[1])
    f.close()
    #print(D)
    count = 0
    for k in D.keys():
        count += howManyContain(D, k, 'shiny gold')
    return count


def howManyContain(D, bag, target):
    count = 0
    for b in D[bag]:
        if b == target:
             return 1
        else:
            count += howManyContain(D, b, target)
    return count != 0



def f2():
    f = open('input.txt', 'r')
    D = {}
    for line in f.readlines():
        match = re.match(r'(.*) bags contain (?:no other bags.|(.*)[.])', line)
        #print('\n',match.groups())
        B = match[1]
        D[B] = []
        if match[2]:
            bag_list = match[2].split(', ')
            for bag in bag_list:
                match = re.match(r'(\d+) ([a-zA-Z]* [a-zA-Z]*) bags?', bag)
                D[B].append((int(match[1]), match[2]))
    f.close()
    #print(D)
    count = numberOfBag(D, 'shiny gold') -1
    return count


def numberOfBag(D, bag):
    count = 1
    for (n,b) in D[bag]:
        count += n * numberOfBag(D, b)
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


