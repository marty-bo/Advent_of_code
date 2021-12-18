
import time
from Graph import Graph


def is_big_cave(cave:str):
    return cave[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def count_paths(graph:Graph, start:str, end:str, twice:bool)->int:
    """
    return the number of paths in the graph <graph> from <start> to <end>.
    The path can visit small caves only once and big caves any numbers of time.
    There is one exception, if <twice> is True, the path can visit one small cave twice.
    """
    def count_paths_rec(graph:Graph, start:str, end:str, inaccessibles:set, viewed:set, path:list, twice:bool):
        path.append(start)
        count = 0
        for vertice in graph.edges.get(start, set()):
            if vertice in inaccessibles:
                continue
            if vertice == end:
                path.append(end)
                # print(','.join(path))
                path.pop()
                count += 1
            elif is_big_cave(vertice):
                count += count_paths_rec(graph, vertice, end, inaccessibles, viewed, path, twice)
            elif vertice not in viewed:
                viewed.add(vertice)
                count += count_paths_rec(graph, vertice, end, inaccessibles, viewed, path, twice)
                viewed.remove(vertice)
            elif vertice in viewed and twice:
                count += count_paths_rec(graph, vertice, end, inaccessibles, viewed, path, False)
        path.pop()
        return count
    
    return count_paths_rec(graph, start, end, set([start]), set(), list(), twice)



def f(twice:bool):
    graph = Graph(dict())

    f = open('input.txt')
    for line in f.readlines():
        line = line.replace('\n','').split('-')
        graph.add_edge((line[0], line[1]))
    f.close()

    paths_count = count_paths(graph, 'start', 'end', twice)

    print('[f]: Twice = %s Paths count = %d' % (twice, paths_count))
    return 0
    



print("########################################")
start_time = time.time()
f(False)
print("----------- %.8s seconds -----------" % (time.time() - start_time))


print("########################################")
start_time = time.time()
f(True)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
