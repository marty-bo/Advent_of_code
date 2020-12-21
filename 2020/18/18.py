
import time





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


# ################################################################
#
# Part 1 - LL1 analyze
#
# ##### Grammar WITHOUT operator priority :
# S → E END
# E → E + F  
# E → E * F  
# E → F
# F → val
# F → ( E )
#
# ##### Without left recursivity :
# R0 : S → E END
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
#     +   *   (   )   val     END
# E               x           x         
# E2              x           x      
# F   x   x       x           x
#
# ##### LL1 :
#     +   *   (   )   val     END
# S           R0      R0
# E           R1      R1
# E2  R2  R3      R4          R4
# F           R6      R5
# 
# ################################################################




# R0 : S → E END
def S_p1(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # E
        r = E_p1(reader)
        # END
        if reader.isEmpty():
            return r
    return -1

# R1 : E → F E2
def E_p1(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # F
        v = F_p1(reader)
        # E2
        r = E2_p1(reader, v)
        return r
    return -1

# R2 : E2 → + F E2 
# R3 : E2 → * F E2
# R4 : E2 → epsilon
def E2_p1(reader, val):
    if reader.isEmpty() or reader.look() == ')':
        # epsilon
        return val
    elif reader.look() == '+':
        # +
        reader.read()
        # F
        val += F_p1(reader)
        # E2
        r = E2_p1(reader, val)
        return r
    elif reader.look() == '*':
        # *
        reader.read()
        # F
        val *= F_p1(reader)
        # E2
        r = E2_p1(reader, val)
        return r
    return -1

# R5 : F → val
# R6 : F → ( E )
def F_p1(reader):
    if reader.look() == '(':
        # (
        reader.read()
        # E
        r = E_p1(reader)
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
        res.append(S_p1(Reader(expr)))
    return sum(res)







# ################################################################
#
# Part 2 - LL1 analyze
#
# ##### Grammar WITH operator priority :
# Attention '+' is more priority than '*'
# S → E END
# E → E * T 
# E → T  
# T → T + F  
# T → F
# F → val
# F → ( E )
#
# ##### Without left recursivity :
# R0 : S → E END
# R1 : E → T E2
# R2 : E2 → + T E2
# R3 : E2 → epsilon
# R4 : T → F T2
# R5 : T2 → * F T2
# R6 : T2 → epsilon
# R7 : F → val
# R8 : F → ( E )
#
# ##### first :
#     +   *   (   )   val     epsilon
# E           x       x
# E2      x                   x
# T           x       x
# T2  x                       x
# F           x       x
#
# ##### next :
#     +   *   (   )   val     END
# E               x           x         
# E2              x           x    
# T       x       x           x
# T2      x       x           x
# F   x   x       x           x
#
# ##### LL1 :
#     +   *   (   )   val     END
# S           R0      R0
# E           R1      R1
# E2      R2      R3          R3
# T           R4      R4
# T2  R5  R6      R6          R6
# F           R6      R5
# 
# ################################################################

# R0 : S → E END
def S_p2(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # E
        r = E_p2(reader)
        # END
        if reader.isEmpty():
            return r
    return -1

# R1 : E → T E2
def E_p2(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # T
        v = T_p2(reader)
        # E2
        r = E2_p2(reader, v)
        return r
    return -1


# R2 : E2 → * T E2
# R3 : E2 → epsilon
def E2_p2(reader, val):
    if reader.isEmpty() or reader.look() == ')':
        # epsilon
        return val
    elif reader.look() == '*':
        # *
        reader.read()
        # T
        val *= T_p2(reader)
        # E2
        r = E2_p2(reader, val)
        return r
    return -1


# R4 : T → F T2
def T_p2(reader):
    if reader.look() == '(' or isVal(reader.look()):
        # F
        v = F_p2(reader)
        # T2
        r = T2_p2(reader, v)
        return r
    return -1



# R5 : T2 → + F T2
# R6 : T2 → epsilon
def T2_p2(reader, val):
    if reader.isEmpty() or reader.look() == ')' or reader.look() == '*':
        # epsilon
        return val
    elif reader.look() == '+':
        # +
        reader.read()
        # F
        val += F_p2(reader)
        # T2
        r = T2_p2(reader, val)
        return r
    return -1


# R5 : F → val
# R6 : F → ( E )
def F_p2(reader):
    if reader.look() == '(':
        # (
        reader.read()
        # E
        r = E_p2(reader)
        # )
        reader.read()
        return r
    elif isVal(reader.look()):
        # val
        r = int(reader.read())
        return r
    return -1

def f2(fileName):
    f = open(fileName, 'r')
    expressions = [ list(l.replace(' ', '').replace('\n', '')) for l in f.readlines()]
    # print(expressions)
    res = []
    for expr in expressions:
        res.append(S_p2(Reader(expr)))
    return sum(res)


# ####### MAIN #######
f = 'input.txt'

# Part 1
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))

# Part 2
start_time = time.time()
print(f2(f))
print("--- %s seconds ---" % (time.time() - start_time))
