
import time







def f1(fileName):
    f = open(fileName, 'r')
    nums = []
    # rules
    while 1:
        l = f.readline()
        if l.split() == []:
            break
        nums.append([[int(i) for i in l.split(':')[1].split()[0].split('-')], [int(i) for i in l.split(':')[1].split()[2].split('-')]])

    # 'your ticket:'
    f.readline()
    # your ticket values
    your_ticket = [int(i) for i in f.readline().split()[0].split(',')]

    # '\n'
    f.readline()

    # 'nearby tickets:'
    f.readline()
    # nearby tickets values
    invalid = []
    while 1:
        l = f.readline().split()
        if l == []:
            break
        ticket = [int(i) for i in l[0].split(',')]
        for v in ticket:
            valid = False
            for [[rmin1, rmax1], [rmin2, rmax2]] in nums:
                if (v >= rmin1 and v <= rmax1) or (v >= rmin2 and v <= rmax2):
                    valid = True
                    break
            if not valid:
                invalid.append(v)
    return sum(invalid)








def isTicketValid(ticket: list, rules: dict) -> int:
    for v in ticket:
        valid = False
        for [[rmin1, rmax1], [rmin2, rmax2]] in rules.values():
            if (v >= rmin1 and v <= rmax1) or (v >= rmin2 and v <= rmax2):
                valid = True
                break
        if not valid:
            return 0
    return 1


def isValidField(val: int, field: list) -> int:
    if (val >= field[0][0] and val <= field[0][1]) or (val >= field[1][0] and val <= field[1][1]):
        return 1
    return 0




def f2(fileName, fieldtarget):
    f = open(fileName, 'r')
    rules = {} # id = field // data = range
    while 1:
        l = f.readline()
        if l.split() == []:
            break
        rules[l.split(':')[0]] = [[int(i) for i in l.split(':')[1].split()[0].split('-')], [int(i) for i in l.split(':')[1].split()[2].split('-')]]
    # print(rules)

    # 'your ticket:'
    f.readline()
    # your ticket values
    your_ticket = [int(i) for i in f.readline().split()[0].split(',')]

    # '\n'
    f.readline()

    # 'nearby tickets:'
    f.readline()
    # nearby tickets values
    valid_ticket = []
    while 1:
        l = f.readline().split()
        if l == []:
            break
        ticket = [int(i) for i in l[0].split(',')]
        if isTicketValid(ticket, rules):
            valid_ticket.append(ticket)
    # print(valid_ticket)

    valid_field = {f_name : [i for i in range(len(ticket))] for f_name in rules.keys()}
    # print(valid_field)

    
    for ticket in valid_ticket:
        for field in rules.keys():
            for index in valid_field[field]:
                if not isValidField(ticket[index], rules[field]):
                    valid_field[field].remove(index)
    
    change = 1
    while change:
        change = 0
        for field in rules.keys():
            if len(valid_field[field]) == 1:
                v = valid_field[field][0]
                for f in rules.keys():
                    if v in valid_field[f] and f != field:
                        valid_field[f].remove(v)
                        change = 1
    
    res = 1
    for field in valid_field.keys():
        if fieldtarget in field:
            res *= your_ticket[valid_field[field][0]]
    return res

# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2(f, 'departure'))
print("--- %s seconds ---" % (time.time() - start_time))

