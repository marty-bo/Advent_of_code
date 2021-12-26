
import time
from Node import Node



def reduce(tree : Node):
    while True:
        dfsl = tree.depth_first_search_list()
        # explode
        exploded = False
        for i in range(len(dfsl)):
            # if a sailfish number need to be explode
            if dfsl[i][1] >= 4 and dfsl[i][0].is_node:
                (left, right) = dfsl[i][0].explode()
                if left.is_node or right.is_node:
                    print('Error')
                    exit(0)
                # increase the first value on the left
                j = i-2
                while j >= 0:
                    if dfsl[j][0].is_node:
                        j -= 1
                    else:
                        dfsl[j][0].value += left.value
                        break
                # increase the first value on the right
                j = i+2
                while j < len(dfsl):
                    if dfsl[j][0].is_node:
                        j += 1
                    else:
                        dfsl[j][0].value += right.value
                        break
                exploded = True
                break
        if exploded:
            continue

        # split
        if tree.split():
            continue
        break
    return tree



def str_to_Node(line):
    nodes = []
    for c in line:
        if c == '[':
            pass
        elif c == ',':
            pass
        elif c == ']':
            n1 = nodes.pop()
            n2 = nodes.pop()
            nodes.append(Node(True, 0, n2, n1))
        else:
            nodes.append(Node(False, int(c), None, None))
    return nodes.pop()



def f1():

    f = open('input.txt')
    line = f.readline().replace('\n','')
    tree = str_to_Node(line)
    for line in f.readlines():
        line = line.replace('\n','')
        tree = Node(True, 0, tree, str_to_Node(line))
        reduce(tree)
    f.close()


    print(tree.to_string())

    print('[f1]: Magnitude = %d' % (tree.magnitude()))
    return
    


def f2():

    trees = []
    f = open('input.txt')
    for line in f.readlines():
        line = line.replace('\n','')
        trees.append(str_to_Node(line))
    f.close()

    max_magnitude = 0
    for i in range(len(trees)):
        for j in range(len(trees)):
            if i == j:
                continue
            tmp_tree = Node(True, 0, trees[i].clone(), trees[j].clone())
            reduce(tmp_tree)
            max_magnitude = max(max_magnitude, tmp_tree.magnitude())

    print('[f2]: Max magnitude = %d' % (max_magnitude))
    return


print("########################################")
start_time = time.time()
f1()
print("----------- %.8s seconds -----------" % (time.time() - start_time))

print("########################################")
start_time = time.time()
f2()
print("----------- %.8s seconds -----------" % (time.time() - start_time))
