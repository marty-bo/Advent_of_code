
import time
import math


def can_reach_target_area(vel_x, vel_y, target_area_x_left, target_area_x_right, target_area_y_bottom, target_area_y_top):
    # we can search some shortcuts to eliminate invalid velocities instead of simulate them
    # ...
    pos_x = 0
    pos_y = 0
    while pos_x <= target_area_x_right and pos_y >= target_area_y_bottom:
        pos_x += vel_x
        pos_y += vel_y

        vel_x = max(0, vel_x - 1)
        vel_y -= 1

        if pos_x >= target_area_x_left and pos_x <= target_area_x_right and pos_y >= target_area_y_bottom and pos_y <= target_area_y_top:
            return True
    return False



def f(debug=False):

    f = open('input.txt')
    line = f.readline()
    f.close()

    line = line.replace('target area: x=','').replace(', y=',',').replace('..',',')
    [target_area_x_left, target_area_x_right, target_area_y_bottom, target_area_y_top] = [int(n) for n in line.split(',')] 

    print('target_area_x_left = %d' % (target_area_x_left))
    print('target_area_x_right = %d' % (target_area_x_right))
    print('target_area_y_bottom = %d' % (target_area_y_bottom))
    print('target_area_y_top = %d' % (target_area_y_top))

    # the maximum distance D we can reach in the x axis with a velocity in x of N is D = (N*(N+1))/2
    # so N = int(sqrt(D*2))
    min_velocity_x = int(math.sqrt(target_area_x_left*2))

    # with a higher velocity, the probe will just go after the target area
    max_velocity_x = target_area_x_right

    # with a lower velocity, the probe will just go after the target area
    # we can choose min_velocity_y = 0
    min_velocity_y = - abs(target_area_y_bottom)

    # only if the area_min_y is negative and different to 0
    # with a higher velocity, the probe will just go after the target area
    max_velocity_y = abs(target_area_y_bottom)

    print('min_velocity_x = %d' % (min_velocity_x))
    print('max_velocity_x = %d' % (max_velocity_x))
    print('min_velocity_y = %d' % (min_velocity_y))
    print('max_velocity_y = %d' % (max_velocity_y))

    valid_velocities = []
    for vel_x in range(min_velocity_x, max_velocity_x + 1):
        for vel_y in range(min_velocity_y, max_velocity_y + 1):
            if can_reach_target_area(vel_x, vel_y, target_area_x_left, target_area_x_right, target_area_y_bottom, target_area_y_top):
                valid_velocities.append((vel_x, vel_y))
    
    # print(valid_velocities)
    highest_y_position = 0
    for (vel_x, vel_y) in valid_velocities:
        if vel_y <= 0:
            continue
        highest_y_position = max(highest_y_position, int((vel_y*(vel_y+1))/2))

    print('[f]: Highest y position = %d Numbers of solutions = %d' % (highest_y_position, len(valid_velocities)))

    return
    



print("########################################")
start_time = time.time()
f(debug=False)
print("----------- %.8s seconds -----------" % (time.time() - start_time))
