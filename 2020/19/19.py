
import time



class Item:
    def __init__(self, I_num, line_num, rule_name, rule_p1, rule_p2, log):
        self.I_num = I_num
        self.line_num = line_num
        self.rule_name = rule_name
        self.rule_p1 = rule_p1
        self.rule_p2 = rule_p2
        self.log = log
    def show(self):
        print("| {:3} | {:3} | {:>3} -> {:>7} . {:<7} | {:7} |".format(self.I_num, self.line_num, self.rule_name, ' '.join(self.rule_p1), ' '.join(self.rule_p2), self.log))





class EarleyAlgorithm:
    def __init__(self, word : list, rules : dict, source : str):
        self.items = []
        self.word = word
        self.rules = rules # A->ABC|DEF => {A : [[A,B,C], [D,E,F]]}
        # [fromItem, left rule, right rule before point, right rule after point, info (only for log)]
        self.items.append([Item(0, 0, '', [], [source], 'init')])
    
    def analyze(self) -> int:
        while self.prediction() or self.completion():
            pass
        
        while self.word:
            self.lecture()
            while self.prediction() or self.completion():
                pass
        
        # i = 0
        # for item in self.items:
        #     print('I :', i)
        #     i += 1
        #     print('_'*(50))
        #     for l in item:
        #         l.show()
        #     print('|'+'_'*(48)+'|')
        #     print('\n')
        # print('##########\n')
        return '' in [item.rule_name for item in self.items[-1]]
        
    
    def lecture(self):
        self.items.append([])
        
        c = self.word[0]
        i = len(self.items) - 1
        self.word = self.word[1:]
        for item in self.items[-2]:
            if len(item.rule_p2) and item.rule_p2[0] == c:
                left = item.rule_p1 + [c]
                right = []
                if len(item.rule_p2) > 1:
                    right = item.rule_p2[1:]
                self.items[-1].append(Item(item.I_num, len(self.items[-1]), item.rule_name, left, right, 'L-' + str(i)))
    
    # return the number of prediction added
    def prediction(self) -> int:
        item_num = len(self.items) - 1
        i = 0
        change = 0
        while i < len(self.items[-1]):
            if self.items[-1][i].rule_p2 != [] and self.items[-1][i].rule_p2[0] not in 'ab' and [self.items[-1][i].rule_p2[0], 'P'] not in [[item.rule_name, item.log[0]] for item in self.items[-1]]:
                change += 1
                for r in self.rules[self.items[-1][i].rule_p2[0]]:
                    self.items[-1].append(Item(item_num, len(self.items[-1]), self.items[-1][i].rule_p2[0], [], r, 'P-' + str(i)))
            i += 1
        return change

    # return the number of completion added
    def completion(self) -> int:
        change = 0
        i = 0
        while i < len(self.items[-1]):
            if self.items[-1][i].rule_p2 == []:
                item_num = self.items[-1][i].I_num
                j = 0
                while j < len(self.items[item_num]):
                    if self.items[item_num][j].rule_p2 != [] and self.items[item_num][j].rule_p2[0] == self.items[-1][i].rule_name and  [self.items[item_num][j].rule_name, self.items[item_num][j].rule_p1 + [self.items[item_num][j].rule_p2[0]], self.items[item_num][j].rule_p2[1:]] not in [[item.rule_name, item.rule_p1, item.rule_p2] for item in self.items[-1]]:
                        left = self.items[item_num][j].rule_p1 + [self.items[-1][i].rule_name]
                        if self.items[item_num][j].rule_p2 != []:
                            right = self.items[item_num][j].rule_p2[1:]
                        else:
                            right = []
                        self.items[-1].append(Item(self.items[item_num][j].I_num, len(self.items[-1]), self.items[item_num][j].rule_name, left, right, 'C-' + str(i) + '-' + str(j)))
                        change += 1
                    j += 1
            i += 1
            if i > 20:
                break
        return change


def readRules(f) -> dict:
    rules = {}
    l = f.readline()
    while l.split():
        [left, right] = l.replace('\n', '').replace('"', '').split(':')
        right = right.split('|')
        rules[left] = [list(r.split()) for r in right]
        l = f.readline()
    return rules


def f1(fileName):
    f = open(fileName, 'r')
    rules = readRules(f)
    l = f.readline().split()
    n = 0
    while l:
        earley = EarleyAlgorithm(l[0], rules, '0')
        n += earley.analyze()
        # print(n)
        l = f.readline().split()
    return n


# ####### MAIN #######
f = 'input_part1.txt'

# Part 1-2 - Early Algorithm
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

