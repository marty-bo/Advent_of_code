
import time

class passportValid():
    def __init__(self):
        # Store data from a passport : 0=invalid or unchecked, 1=valid
        self.field = {
            "ecl":0,
            "pid":0,
            "eyr":0,
            "hcl":0,
            "byr":0,
            "iyr":0,
            "cid":0,
            "hgt":0,
        }
        # store the function to call to check value of each field (part 2)
        self.func = {
            "ecl": self.checkECL,
            "pid": self.checkPID,
            "eyr": self.checkEYR,
            "hcl": self.checkHCL,
            "byr": self.checkBYR,
            "iyr": self.checkIYR,
            "cid": self.checkCID,
            "hgt": self.checkHGT,
        }
    
    def reset(self):
        self.field = {
            "ecl":0,
            "pid":0,
            "eyr":0,
            "hcl":0,
            "byr":0,
            "iyr":0,
            "cid":0,
            "hgt":0,
        }
    
    def checkECL(self, v):
        try:
            if v in 'amb blu brn gry grn hzl oth'.split():
                return 1
        except:
            return 0
        return 0
    
    def checkPID(self, v):
        try:
            if len(v) == 9:
                a = int(v)
                return 1
        except:
            return 0
        return 0
    
    def checkEYR(self, v):
        try:
            if len(v) != 4:
                return 0
            else:
                y = int(v)
                if y >= 2020 and y <= 2030:
                    return 1
        except:
            return 0
        return 0
    
    def checkHCL(self, v):
        try:
            if v[0] != '#':
                return 0
            for c in v[1:]:
                if not (c in '0123456789abcdef'):
                    return 0
                return 1
        except:
            return 0
        return 0
    
    def checkBYR(self, v):
        try:
            if len(v) != 4:
                return 0
            else:
                y = int(v)
                if y >= 1920 and y <= 2002:
                    return 1
        except:
            return 0
        return 0
    
    def checkIYR(self, v):
        try:
            if len(v) != 4:
                return 0
            else:
                y = int(v)
                if y >= 2010 and y <= 2020:
                    return 1
        except:
            return 0
        return 0
    
    def checkCID(self, v):
        # Ignored, missing or not.
        return 1
    
    def checkHGT(self, v):
        try:
            if v[-1:-3:-1][::-1] == 'cm':
                h = int(v[0:3])
                if h >= 150 and h <= 193:
                    return 1
            elif v[-1:-3:-1][::-1] == 'in':
                h = int(v[0:2])
                if h >= 59 and h <= 76:
                    return 1  
        except:
            return 0
        return 0
    
    def valid(self):
        return (self.field["ecl"] + self.field["pid"] + self.field["eyr"] + self.field["hcl"] + self.field["byr"] + self.field["iyr"] + self.field["hgt"]) == 7








def f1():
    f = open('input.txt', 'r')
    passport = passportValid()
    valid = 0
    for line in f.readlines():
        if line.split() == []:
            # print(passport.field)
            if passport.valid():
                valid += 1
            passport.reset()
            continue
        else:
            line = line.split()
            for l in line:
                passport.field[l.split(':')[0]] = 1
    if passport.valid():
        valid += 1
    f.close()
    return valid



def f2():
    f = open('input.txt', 'r')
    passport = passportValid()
    valid = 0
    for line in f.readlines():
        if line.split() == []:
            # print(passport.field)
            if passport.valid():
                valid += 1
            passport.reset()
            continue
        else:
            line = line.split()
            for l in line:
                passport.field[l.split(':')[0]] = passport.func[l.split(':')[0]](l.split(':')[1])
    if passport.valid():
        valid += 1
    f.close()
    return valid





# ####### MAIN #######

# Part 1
start_time = time.time()
print(f1())
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2())
print("--- %s seconds ---" % (time.time() - start_time))
