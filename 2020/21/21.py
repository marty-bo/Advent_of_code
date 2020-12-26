import time



def f1(fileName):
    f = open(fileName, 'r')
    L = [] # [[list of food], [contains]]
    for l in f.readlines():
        l = l.split('(')
        L.append([l[0].split(), l[1].replace(')','').replace(',','').split('contains')[1].split()])
    
    D = {} # food_name : {all possible traduction}
    for l in L:
        for food_name in l[1]:
            if not food_name in D.keys():
                D[food_name] = set(l[0])
            else:
                D[food_name].update(l[0])

    for l in L:
        for food_name in l[1]:
            tmp = []
            for e in l[0]:
                if e in D[food_name]:
                    tmp.append(e)
            D[food_name] = tmp
            if len(tmp) == 1:
                for k in D.keys():
                    if k != food_name:
                        if tmp[0] in D[k]:
                            D[k].remove(tmp[0])
    
    for key in D.keys():
        if len(D[key]) == 1:
            for k in D.keys():
                if k != key:
                    if D[key][0] in D[k]:
                        D[k].remove(D[key][0])
    
    allergen = [v[0] for v in D.values()]

    no_allergen = 0
    for l in L:
        for e in l[0]:
            if not e in allergen:
                no_allergen += 1
    
    allergen = ','.join([t for (f,t) in sorted([(key, D[key][0]) for key in D.keys()])])

    return no_allergen, allergen

# ####### MAIN #######
f = 'input.txt'

# Part 1-2
start_time = time.time()
res1, res2 = f1(f)
print(res1)
print(res2)
print("--- %s seconds ---" % (time.time() - start_time))
