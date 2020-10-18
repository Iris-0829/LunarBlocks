import pygame
from data_manager import * 
from typing import List, Tuple
import math
def CheckCircle(posClick, input_port: Tuple[Tuple[int]])-> int:
    for i in range(0, len(input_port)):
        x = (posClick[0] - input_port[i][0])*(posClick[0] - input_port[i][0])
        y = (posClick[1] - input_port[i][1])*(posClick[1] - input_port[i][1])
        if 5 > math.sqrt(x + y):
            return i
        
    return -1    
          
def drawAng(screen, angle, pos):
    nar=pygame.transform.rotate(arrow,angle)
    nrect=nar.get_rect(center=pos)
    screen.blit(nar, nrect)
def make_arrow(screen, shape1, shape2, i , j):
    '''
    Shape1 and Shape2 are 3 tuples of (Rect_obj, shape_img, operatorNode)
    along with ith and jth position for the hit
    '''
    pos1 = shape1[2].input_ports[i]
    pos2 = shape2[2].output_ports[j]
    pygame.draw.line(screen, (255,255,255), pos1, pos2)
    add_line(shape1, shape2, i, j)
    arrow = pygame.Surface((25,25))
    arrow.fill((255,255,255))
    pygame.draw.line(arrow, (0,0,0), (0,0), (25/2,25/2))
    pygame.draw.line(arrow, (0,0,0), (0,25), (25/2,25/2))
    arrow.set_colorkey((0, 0, 0))       
    angle=math.atan2(-(pos1[1]-pos2[1]), pos1[0]-pos2[0])
    ##Note that in pygame y=0 represents the top of the screen
    ##So it is necessary to invert the y coordinate when using math
    angle=math.degrees(angle)
    angle+=180
    drawAng(angle, pos2, arrow)
                    
def add_line(shape1, shape2, i: int , j: int):
    # create line between shapes.
    global SHAPE_ID
    global LINE_ID
    try:
        shapeId_1 = get_shape_id(shape1)
        shapeId_2 = get_shape_id(shape2)
        edges[shapeId_1].append(LINE_ID)
        edges[shapeId_2].append(LINE_ID)
        directed_graph[shapeId_1].append(shapeId_2)
        if i != -1 and j != -1:
            lines[LINE_ID] = [shape1[2].input_port[i], shape2[2].output_port[j]]
        LINE_ID += 1
    except:
        print("addLine(), problem!")
    return


def add_shape(Rect_obj, shape_img, operator):
    global SHAPE_ID
    shapes[SHAPE_ID] = [Rect_obj, shape_img, operator]
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

def graph_draw(event, screen):
    global dragging, dragged, dragged_id, dragged_init_pos, selected, offset_x, offset_y, connected_lines
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if not dragging:
                for shape_id in shapes:
                    shape = shapes[shape_id][0]
                    if(shape.collidepoint(event.pos)):
                        if(selected != shape) and (selected is not None):
                            # draws the line and deselect shape
                            add_line(selected, shape, -1, -1)
                            selected = None
                            shapes[dragged_id][1] = shapes[dragged_id][2].draw(screen)[1]
                            break
                        else:
                            dragged_id = get_shape_id(shape)
                            #if(shapes[dragged_id][2].draggable == True):
                            dragging = True
                            dragged = shape
                            dragged_init_pos = (shape.x, shape.y)

                            # Gets all lines connected to shape, along with which end is connected to our shape.
                            connected_lines = get_connected_lines(dragged_id, dragged_init_pos)

                            m_x, m_y = event.pos
                            offset_x = shape.x - m_x
                            offset_y = shape.y - m_y
                            break

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            if(dragged is not None and dragged_init_pos is not None):
                if(dragged.x == dragged_init_pos[0] and dragged.y == dragged_init_pos[1]):
                    selected = dragged
                    s = shapes[dragged_id]
                    s[1] = s[2].selected()[1]

            dragging = False
            dragged = None
            dragged_init_pos = None 

    if event.type == pygame.MOUSEMOTION:
        if dragging:
            #move shape and snap to grid
            print("moving")
            m_x, m_y = event.pos
            p_x = round((m_x + offset_x) /
                            grid_square_size)*grid_square_size
            p_y = round((m_y + offset_y) /
                            grid_square_size)*grid_square_size

            #Make sure shape is in bounds
            if (p_x < (GAME_FIELD_POS_X + GAME_FIELD_WIDTH) and p_x > (GAME_FIELD_POS_X) and p_y > GAME_FIELD_POS_Y):
                print(dragged)
                dragged.x = p_x
                dragged.y = p_y
            #move our line properly
            for key in connected_lines:
                idx = connected_lines[key]
                line = lines[key]
                line[idx] = (dragged.x, dragged.y)
