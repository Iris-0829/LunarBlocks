import pygame
import pygame_gui
import math
from enum import Enum
from collections import defaultdict
from components.Addition import *
from components.Subtraction import *
#from operator_select import *


rad = math.pi/180
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
grid_square_size = 15  # 15x15px
FPS = 30
LINE_ID = 0
SHAPE_ID = 0

operator_set = []
operand_set = []
shapes = defaultdict(list)
lines = {}
edges = defaultdict(list)


pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()
ui_man = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "theme.json")


clock = pygame.time.Clock()

# TODO: clean this up
# It doesn't really need to be in this file.
# I'll keep it around for now though. 


def add_line(shape1, shape2):
    # create line between shapes.
    global SHAPE_ID
    global LINE_ID
    try:
        shapeId_1 = get_shape_id(shape1)
        shapeId_2 = get_shape_id(shape2)
        edges[shapeId_1].append(LINE_ID)
        edges[shapeId_2].append(LINE_ID)
        lines[LINE_ID] = [(shape1.x, shape1.y), (shape2.x, shape2.y)]
        LINE_ID += 1
    except:
        print("addLine(), problem!")
    return


def add_shape(shape, shape_img, operator):
    global SHAPE_ID
    shapes[SHAPE_ID] = [shape, shape_img, operator]
    SHAPE_ID += 1


def get_shape_id(shape):
    global SHAPE_ID
    for id in shapes:
        if(shapes[id][0] == shape):
            return id
    shapes[SHAPE_ID] = shape[0]
    SHAPE_ID += 1
    return SHAPE_ID - 1


def get_connected_lines(shape_id, shape_pos):
    d = {}
    for line_id in edges[shape_id]:
        line = lines[line_id]
        if line[0] == shape_pos:
            d[line_id] = 0
        else:
            d[line_id] = 1
    return d


# From https://stackoverflow.com/questions/56295712/how-to-draw-a-dynamic-arrow-in-pygame
def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad))))


# =======
# For Testing Purposes
# ======
for i in range(2):
    add = Addition(0, i*10, i*10)
    s = add.draw()
    add_shape(s[0], s[1], add)
for i in range(2):
    sub = Subtraction(0, i*10, i*10)
    s = sub.draw()
    add_shape(s[0], s[1], sub)

game_panel_rect = pygame.Rect(
    SCREEN_WIDTH//5, SCREEN_HEIGHT//2, (4*SCREEN_WIDTH)//5, SCREEN_HEIGHT//2)
operands_panel_rect = pygame.Rect(
    SCREEN_WIDTH//5, 0, (4*SCREEN_WIDTH//5), (SCREEN_HEIGHT//2))
operators_panel_rect = pygame.Rect(0, 0, SCREEN_WIDTH//5, SCREEN_HEIGHT)



def menu_click(event):
    pass


def draw_menu():
    pass


game_panel = pygame_gui.elements.UIPanel(
    relative_rect=game_panel_rect,
    starting_layer_height=0,
    manager=ui_man
)
operands_panel = pygame_gui.elements.UIPanel(
    relative_rect=operands_panel_rect,
    starting_layer_height=0,
    manager=ui_man
)
operators_panel = pygame_gui.elements.UIPanel(
    relative_rect=operators_panel_rect,
    starting_layer_height=0,
    manager=ui_man
)
ui_man.set_visual_debug_mode(True)
#========


def game_loop():
    dragging = False
    dragged = None
    dragged_init_pos = None
    dragged_id = -1

    line_num = -1

    selected = None
    drawing = False
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # This is how we would create an "add/delete" button:
                    # if(button.collidepoint(event.pos)):
                    #    operatorSet.append(pygame.Rect(200, 200, 30, 30))
                    # else:
                    if not dragging:
                        for shape_id in shapes:
                            shape = shapes[shape_id][0]
                            if(shape.collidepoint(event.pos)):
                                if(selected != shape) and (selected is not None):
                                    # draws the line and deselect shape
                                    add_line(selected, shape)
                                    selected = None
                                    shapes[dragged_id][1] = shapes[dragged_id][2].draw()[1]
                                    break
                                else:
                                    # Begins the dragging sequence.
                                    dragging = True
                                    dragged = shape
                                    dragged_id = get_shape_id(dragged)
                                    dragged_init_pos = (shape.x, shape.y)
                                    # Gets all lines connected to shape, along with which end is connected to our shape.
                                    connected_lines = get_connected_lines(
                                        dragged_id, dragged_init_pos)

                                    m_x, m_y = event.pos
                                    offset_x = shape.x - m_x
                                    offset_y = shape.y - m_y
                                    break

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if(dragged is not None and dragged_init_pos is not None):
                        if(dragged.x == dragged_init_pos[0] and dragged.y == dragged_init_pos[1]):
                            selected = dragged
                            # This is a convoluted way of making the shape into the "selected" version.
                            s = shapes[dragged_id]
                            s[1] = s[2].selected()[1]

                    dragging = False
                    dragged = None
                    dragged_init_pos = None

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    #move shape and snap to grid
                    m_x, m_y = event.pos
                    dragged.x = round((m_x + offset_x) /
                                      grid_square_size)*grid_square_size
                    dragged.y = round((m_y + offset_y) / 
                                      grid_square_size)*grid_square_size
                    
                    #move our line properly
                    for key in connected_lines:
                        idx = connected_lines[key]
                        line = lines[key]
                        line[idx] = (dragged.x, dragged.y)

            ui_man.process_events(event)

            ui_man.update(time_delta)

            screen.fill((255, 255, 255))

            for shape_id in shapes:
                screen.blit(shapes[shape_id][1], shapes[shape_id][0])

            for line in lines:  
                arrow(screen, (0,0,0), (0,0,0), lines[line][0], lines[line][1], 10, 5)
            
            ui_man.draw_ui(screen)
            pygame.display.flip()

game_loop()
pygame.quit()
