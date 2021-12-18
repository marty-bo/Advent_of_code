
import time
from Cellular_automata import Cellular_automata as CA

## -- Pygame
# import pygame
# from pygame.locals import *
## Pygame --


## -- Pygame
# def visualize(CELLS, SCREEN, CELL_WIDTH_SIZE, CELL_HEIGHT_SIZE, CLOCK, FRAME_RATE):
#     for i in range(len(CELLS)):
#         for j in range(len(CELLS[i])):
#             color_val = int(min(CELLS[i][j].energy, 10) * 25.5)
#             color = (color_val, color_val, color_val)
#             pygame.draw.rect(SCREEN, color, Rect(i*CELL_WIDTH_SIZE, j*CELL_HEIGHT_SIZE, CELL_WIDTH_SIZE, CELL_HEIGHT_SIZE))
#     CLOCK.tick(FRAME_RATE)
#     pygame.display.flip()
## Pygame --

def f1(steps, stop_when_stabilization=True):

    f = open('input.txt')
    CELLS = [[CA(int(energy), []) for energy in line.replace('\n','')] for line in f.readlines()]
    f.close()

    for i in range(len(CELLS)):
        for j in range(len(CELLS[i])):
            for ii in (-1,0,1):
                if i+ii < 0 or i+ii >= len(CELLS):
                    continue
                for jj in (-1,0,1):
                    if ii == 0 and jj == 0:
                        continue
                    if j+jj < 0 or j+jj >= len(CELLS[i+ii]):
                        continue
                    CELLS[i][j].add_neighbor(CELLS[i+ii][j+jj])
    
    # print('Before any steps:',*[''.join([str(CELLS[i][j].energy) for j in range(len(CELLS[i]))]) for i in range(len(CELLS))], sep='\n', end='\n\n')


    ## -- Pygame
    # SCREEN_SIZE = (512, 512)
    # CELLS_WIDTH = 10
    # CELLS_HEIGHT = 10
    # CELL_WIDTH_SIZE = SCREEN_SIZE[0] / CELLS_WIDTH
    # CELL_HEIGHT_SIZE = SCREEN_SIZE[1] / CELLS_HEIGHT
    # SCREEN = pygame.Surface
    # CLOCK = pygame.time.Clock()
    # FRAME_RATE = 100
    # pygame.init()
    # SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    # visualize(CELLS, SCREEN, CELL_WIDTH_SIZE, CELL_HEIGHT_SIZE, CLOCK, FRAME_RATE)
    ## Pygame --

    total_flashes = 0
    step = 0
    all_flash_step = None
    while step < steps or (stop_when_stabilization and all_flash_step == None):
        flashes = 0
        for i in range(len(CELLS)):
            for j in range(len(CELLS[i])):
                CELLS[i][j].increase_energy()
        for i in range(len(CELLS)):
            for j in range(len(CELLS[i])):
                flashes += CELLS[i][j].flashes()
        if flashes == 100:
            all_flash_step = step+1
        total_flashes += flashes
        for i in range(len(CELLS)):
            for j in range(len(CELLS[i])):
                CELLS[i][j].end_step()

        ## -- Pygame
        # visualize(CELLS, SCREEN, CELL_WIDTH_SIZE, CELL_HEIGHT_SIZE, CLOCK, FRAME_RATE)
        # CLOCK.tick(FRAME_RATE)
        # pygame.display.flip()
        ## Pygame --
        
        step += 1
        # print('After step %d:'%(step),*[''.join([str(CELLS[i][j].energy) for j in range(len(CELLS[i]))]) for i in range(len(CELLS))], sep='\n', end='\n\n')
    if stop_when_stabilization:
        print('[f1]: Total Flashes = %d All flash step = %d' % (total_flashes, all_flash_step))
    else:
        print('[f1]: Total Flashes = %d' % (total_flashes))
    
    return
    


print("########################################")
start_time = time.time()
f1(steps=100, stop_when_stabilization=False)
print("--------- %.7s seconds ---------" % (time.time() - start_time))

