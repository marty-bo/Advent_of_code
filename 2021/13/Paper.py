

class Paper():

    def __init__(self, dots:set):
        self.dots = set(dots)
    
    def fold(self, instruction:set):
        def fold_dot(dot_coord, fold_coord):
            if dot_coord < fold_coord:
                return dot_coord
            return fold_coord - (dot_coord - fold_coord)

        tmp_dots = set()
        axis = instruction[0]
        fold_coord = instruction[1]
        # fold along x axis
        if axis == 'x':
            for dot in self.dots:
                tmp_dots.add((fold_dot(dot[0], fold_coord), dot[1]))
        # fold along y axis
        elif axis == 'y':
            for dot in self.dots:
                tmp_dots.add((dot[0], fold_dot(dot[1], fold_coord)))
        
        self.dots = tmp_dots
        return
    
    def count_dots(self):
        return len(self.dots)
    
    def to_string(self):
        width = 0
        height = 0
        for x,y in self.dots:
            if x > width:
                width = x
            if y > height:
                height = y
        width += 1
        height += 1
        res = [['.' for j in range(width)] for i in range(height)]
        for x,y in self.dots:
            res[y][x] = '#'
        return '\n'.join([''.join(res[i]) for i in range(height)])


if __name__ == '__main__':
    paper = Paper({(10, 4), (10, 1)})
    print(paper.to_string(),end='\n\n')
    paper.fold(('y', 2))
    print(paper.to_string())