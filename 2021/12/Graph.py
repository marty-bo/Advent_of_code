


class Graph:
    def __init__(self, edges:dict):
        self.edges = edges

    def add_edge(self, edge:tuple):
        # A -> B
        if self.edges.get(edge[0]) == None:
            self.edges[edge[0]] = {edge[1]}
        else:
            self.edges.get(edge[0]).add(edge[1])

        # B -> A
        if self.edges.get(edge[1]) == None:
            self.edges[edge[1]] = {edge[0]}
        else:
            self.edges.get(edge[1]).add(edge[0])


if __name__ == '__main__':
    graph = Graph(dict())
    graph.add_edge(('A', 'B'))
    graph.add_edge(('B', 'B'))
    graph.add_edge(('B', 'C'))
    print(graph.edges)
    