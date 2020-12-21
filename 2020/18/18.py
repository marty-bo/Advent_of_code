
import time



# ################################################################
#
# Part 1 - LL1 analyze
#
# ##### Grammar :
# R0 : S → E [EOL/EOF]
# R1 : E → E + F  
# R2 : E → E * F  
# R3 : E → F
# R4 : F → val
# R5 : F → ( E )
#
# ##### Without left recursivity :
# R0 : S → E [EOL/EOF]
# R1 : E → F E2
# R2 : E2 → + F E2 
# R3 : E2 → * F E2
# R4 : E2 → epsilon
# R5 : F → val
# R6 : F → ( E )
#
# ##### first :
#     +   *   (   )   val   epsilon
# E           x       x
# E2  x   x                 x
# F           x       x
#
# ##### next :
#     +   *   (   )   val     [EOL/EOF]
# E               x           x         
# E2              x           x      
# F   x   x       x           x
#
# ##### LL1 :
#     +   *   (   )   val     [EOL/EOF]
# S           R0      R0
# E           R1      R1
# E2  R2  R3      R4          R4
# F           R6      R5
# 
# ################################################################


class Reader:
    def __init__(self, expr : list):
        self.expr = expr
    def read(self):
        return self.expr.pop(0)
    def look(self):
        return self.expr[0]
    def isEmpty(self):
        return self.expr == []


def isVal(str_):
    try:
        int(str_)
        return 1
    except:
        return 0

# R0 : S → E [EOL/EOF]
def S(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # E
        r = E(reader)
        # [EOL/EOF]
        if reader.isEmpty():
            return r
    return -1

# R1 : E → F E2
def E(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # F
        v = F(reader)
        # E2
        r = E2(reader, v)
        return r
    return -1

# R2 : E2 → + F E2 
# R3 : E2 → * F E2
# R4 : E2 → epsilon
def E2(reader, val):
    if reader.isEmpty() or reader.look() == ')':
        # epsilon
        return val
    elif reader.look() == '+':
        # +
        reader.read()
        # F
        val += F(reader)
        # E2
        r = E2(reader, val)
        return r
    elif reader.look() == '*':
        # *
        reader.read()
        # F
        val *= F(reader)
        # E2
        r = E2(reader, val)
        return r
    return -1

# R5 : F → val
# R6 : F → ( E )
def F(reader):
    if reader.look() == '(':
        # (
        reader.read()
        # E
        r = E(reader)
        # )
        reader.read()
        return r
    elif isVal(reader.look()):
        # val
        r = int(reader.read())
        return r
    return -1

def f1(fileName):
    f = open(fileName, 'r')
    expressions = [ list(l.replace(' ', '').replace('\n', '')) for l in f.readlines()]
    # print(expressions)
    res = []
    for expr in expressions:
        res.append(S(Reader(expr)))
    return sum(res)



# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))
