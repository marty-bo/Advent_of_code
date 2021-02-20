
import time

def check_collision(wires, wire):
    """return the Manattan distance if a collision is found, -1 otherwise
    wires : list of [level , [min, max]], every element are horizontal or vertical
    wire : [level, [min, max]], this element is the opposite orientation as wires
    """
    min_dist = -1
    for w in wires:
        if (w[0] > wire[1][0]) and (w[0] < wire[1][1]) and (wire[0] > w[1][0]) and (wire[0] < w[1][1]):
            if(min_dist == -1):
                min_dist = abs(w[0]) + abs(wire[0])
            else:
                min_dist = min(min_dist, abs(w[0]) + abs(wire[0]))
    return min_dist


def f1(fileName):
    # wires = [wire1, wire2]
    # wire1 = [horizontal, vertical]
    # wire2 = same as wire1
    # horizontal = [horizontal_level , [min_vertical, max_vertical]]
    # vice versa for vertical
    wires = [[[],[]],[[],[]]]

    closest_cross = -1
    paths = [l.replace('\n', '').split(',') for l in open(fileName).readlines()]
    
    for i in [0,1]:
        other_id = int(not i)
        path = paths[i]
        current_pos = [0,0]
        for p in path:
            direction = p[0]
            length = int(p[1:])
            next_pos = current_pos.copy()
            collision_dist = int
            # print(direction, length)

            if direction == 'U':
                next_pos[1] += length
                collision_dist = check_collision(wires[other_id][0], [current_pos[0], [current_pos[1], next_pos[1]]])
                if (collision_dist != -1):
                    if(closest_cross == -1):
                        closest_cross = collision_dist
                    else:
                        closest_cross = min(closest_cross, collision_dist)
                wires[i][1].append([current_pos[0], [current_pos[1], next_pos[1]]])

            elif direction == 'R':
                next_pos[0] += length
                collision_dist = check_collision(wires[other_id][1], [current_pos[1], [current_pos[0], next_pos[0]]])
                if (collision_dist != -1):
                    if(closest_cross == -1):
                        closest_cross = collision_dist
                    else:
                        closest_cross = min(closest_cross, collision_dist)
                wires[i][0].append([current_pos[1], [current_pos[0], next_pos[0]]])

            elif direction == 'D':
                next_pos[1] -= length
                collision_dist = check_collision(wires[other_id][0], [current_pos[0], [next_pos[1], current_pos[1]]])
                if (collision_dist != -1):
                    if(closest_cross == -1):
                        closest_cross = collision_dist
                    else:
                        closest_cross = min(closest_cross, collision_dist)
                wires[i][1].append([current_pos[0], [next_pos[1], current_pos[1]]])

            elif direction == 'L':
                next_pos[0] -= length
                collision_dist = check_collision(wires[other_id][1], [current_pos[1], [next_pos[0], current_pos[0]]])
                if (collision_dist != -1):
                    if(closest_cross == -1):
                        closest_cross = collision_dist
                    else:
                        closest_cross = min(closest_cross, collision_dist)
                wires[i][0].append([current_pos[1], [next_pos[0], current_pos[0]]])

            # print(current_pos, direction, length, closest_cross, collision_dist)

            current_pos = next_pos
    #print(*wires, sep='\n')
    return closest_cross


# Part 1
f = 'input.txt'
start_time = time.time()
print(f1(f))
print("--- %s seconds ---" % (time.time() - start_time))
