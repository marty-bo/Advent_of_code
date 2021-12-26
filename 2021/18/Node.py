


class Node():

    def __init__(self, is_node, value, left, right):
        self.is_node = is_node
        self.value = value
        self.left = left
        self.right = right
    
    def explode(self):
        self.value = 0
        self.is_node = False
        res = (self.left, self.right)
        self.left = None
        self.right = None
        return res
    
    def split(self):
        if self.is_node:
            if self.left.split():
                return True
            return self.right.split()
        elif self.value >= 10:
            self.left = Node(False, int(self.value/2), None, None)
            self.right = Node(False, self.value - int(self.value/2), None, None)
            self.is_node = True
            self.value = 0
            return True
        return False

    def magnitude(self):
        if self.is_node:
            return 3*self.left.magnitude() + 2*self.right.magnitude() 
        return self.value

    def depth_first_search_list(self, depth=0) -> list:
        if self.is_node:
            res = self.left.depth_first_search_list(depth+1)
            res.extend([(self, depth)])
            res.extend(self.right.depth_first_search_list(depth+1))
            return res
        return [(self, depth)]
    
    def to_string(self):
        if self.is_node:
            return '[' + self.left.to_string() + ',' + self.right.to_string() + ']'
        return str(self.value)
    
    def clone(self):
        if self.is_node:
            return Node(True, 0, self.left.clone(), self.right.clone())
        return Node(False, self.value, None, None)