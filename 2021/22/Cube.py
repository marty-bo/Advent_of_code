
class Cube():
    
    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z
    

    def get_volume(self):
        """Return the volume of the cube."""
        return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1) * (self.max_z - self.min_z + 1)
    
    def is_crossing(self, cube):
        """Return True if the current cube is crossing with cube."""
        # if the cubes are not crossing in the x axis
        if self.max_x < cube.min_x or self.min_x > cube.max_x:
            return False
        
        # if the cubes are not crossing in the y axis
        if self.max_y < cube.min_y or self.min_y > cube.max_y:
            return False
        
        # if the cubes are not crossing in the z axis
        if self.max_z < cube.min_z or self.min_z > cube.max_z:
            return False

        return True

    def cross(self, cube):
        """Return the cross section of the current cube with cube if it exist else None."""
        if self.is_crossing(cube) == False:
            return None

        return Cube(
            max(self.min_x, cube.min_x),
            min(self.max_x, cube.max_x),
            max(self.min_y, cube.min_y),
            min(self.max_y, cube.max_y),
            max(self.min_z, cube.min_z),
            min(self.max_z, cube.max_z)
        )


    def substract(self, cube):
        """Return a list of cube defined by the current cube minus <cube>."""
        
        if self.is_crossing(cube) == False:
            return [self.clone()]
        
        # A cube can be defined by 27 smaller cubes (3x3x3) like a Rubik's Cube (with one at the center).
        # The substract operation consist of build these 27 cubes without the cubes in the cross section.
       
        def build_pairs(c1_min, c1_max, c2_min, c2_max) -> list:
            """Return all pairs of segments with c1_xxx a segment and c2_xxx
            the segment to substract."""
            pairs = list()

            #  first if-elif-else layer: position of c2_min over [c1_min,c1_max]
            # second if-elif-else layer: position of c2_max over [c1_min,c1_max] 

            # full left or on left border
            if c2_min <= c1_min:
                # on left border
                if c2_max == c1_min:
                    pairs.append((c1_min, c2_max))
                    if c2_max+1 <= c1_max:
                        pairs.append((c2_max+1, c1_max))
                # in the middle
                elif c2_max > c1_min and c2_max < c1_max:
                    pairs.append((c1_min, c2_max))
                    if c2_max+1 <= c1_max:
                        pairs.append((c2_max+1, c1_max))
                # on right border
                elif c2_max == c1_max:
                    pairs.append((c1_min, c1_max))
                # full right
                else:
                    pairs.append((c1_min, c1_max))

            # in the middle
            elif c2_min > c1_min and c2_min < c1_max:
                # in the middle
                if c2_max > c1_min and c2_max < c1_max:
                    pairs.append((c1_min, c2_min-1))
                    pairs.append((c2_min, c2_max))
                    pairs.append((c2_max+1, c1_max))
                # on right border
                elif c2_max == c1_max:
                    pairs.append((c1_min, c2_min-1))
                    pairs.append((c2_min, c1_max))
                # full right
                else:
                    pairs.append((c1_min, c2_min-1))
                    pairs.append((c2_min, c1_max))

            # on right border
            elif c2_min == c1_max:
                # on right border
                if c2_max == c1_max:
                    if c2_min-1 >= c1_min:
                        pairs.append((c1_min, c2_min-1))
                    pairs.append((c2_min, c1_max))
                # full right
                else:
                    if c2_min-1 >= c1_min:
                        pairs.append((c1_min, c2_min-1))
                    pairs.append((c2_min, c1_max))

            # full right
            else:
                # full right
                pass

            return pairs
        
        # store all pairs of (min, max) for each cubes for each axis
        x_axis = build_pairs(self.min_x, self.max_x, cube.min_x, cube.max_x)
        y_axis = build_pairs(self.min_y, self.max_y, cube.min_y, cube.max_y)
        z_axis = build_pairs(self.min_z, self.max_z, cube.min_z, cube.max_z)
        
        #print(x_axis, y_axis, z_axis, sep='\n')

        # build all the cubes
        cubes = []
        for (min_x, max_x) in x_axis:
            for (min_y, max_y) in y_axis:
                for (min_z, max_z) in z_axis:
                    c = Cube(min_x, max_x, min_y, max_y, min_z, max_z)
                    if c.is_crossing(cube) == False:
                        cubes.append(c)

        #print(len(cubes))
        #for cube in cubes:
        #    print(cube.to_string())

        return cubes
    

    def fusion(self, cube):
        """If possible return the fusion of the current cube with <cube> else None."""
        
        for (c1, c2) in [(self, cube), (cube, self)]:
            # try to put <c2> on the top of <c1> (Y axis)
            if (c1.min_x == c2.min_x and
                c1.max_x == c2.max_x and
                c1.max_y == c2.min_y and
                c1.min_z == c2.min_z and
                c1.max_z == c2.max_z
                ):
                return Cube(c1.min_x, c1.max_x, min(c1.min_y, c2.min_y), max(c1.max_y, c2.max_y), c1.min_z, c1.max_z)
            
            # try to put <c2> on the right of <c1> (X axis)
            if (c1.max_x == c2.min_x and
                c1.min_y == c2.min_y and
                c1.max_y == c2.max_y and
                c1.min_z == c2.min_z and
                c1.max_z == c2.max_z
                ):
                return Cube(min(c1.min_x, c2.min_x), max(c1.max_x, c2.max_x), c1.min_y, c1.max_y, c1.min_z, c1.max_z)

            # try to put <c2> on the front of <c1> (Z axis)
            if (c1.min_x == c2.min_x and
                c1.max_x == c2.max_x and
                c1.min_y == c2.min_y and
                c1.max_y == c2.max_y and
                c1.max_z == c2.min_z
                ):
                return Cube(c1.min_x, c1.max_x, c1.min_y, c1.max_y, min(c1.min_z, c2.min_z), max(c1.max_z, c2.max_z),)

        return None


    def to_string(self):
        res = ''
        res += 'X='+str(self.min_x)+'..'+str(self.max_x)+' '
        res += 'Y='+str(self.min_y)+'..'+str(self.max_y)+' '
        res += 'Z='+str(self.min_z)+'..'+str(self.max_z)
        return res
    

    def clone(self):
        return Cube(self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z)


if __name__ == '__main__':
    c1 = Cube(36, 37, -23, -23, 14, 34)
    c2 = Cube(36, 37, -23, -23, 14, 34)

    count_c1 = c1.get_volume()
    count_c2 = c2.get_volume()

    cubes = c1.substract(c2)

    count = 0
    for cube in cubes:
        count += cube.get_volume()
        print(cube.to_string())

    print(c1.get_volume(), c2.get_volume(), count)