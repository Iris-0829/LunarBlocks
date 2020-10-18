import pygame
from data_manager import * 
from typing import List, Tuple
import math
def makeList():
    print("Made list yay")
    listforadding = []
    return

def CheckCircle(posClick, input_port: Tuple[Tuple[int]], loc:Tuple[int])-> int:
    for i in range(0, len(input_port)):
        x = (posClick[0] - (input_port[i][0] + loc[0]))*(posClick[0] - (input_port[i][0]+loc[0]))
        y = (posClick[1] - (input_port[i][1] + loc[1]))*(posClick[1] - (input_port[i][1]+loc[1]))
        if 15 > math.sqrt(x + y):
            print("returning hit in port",i)
            return i  
    return -1    
          
def drawAng(screen, angle, pos):
    nar=pygame.transform.rotate(arrow,angle)
    nrect=nar.get_rect(center=pos)
    screen.blit(nar, nrect)
""" def make_arrow(screen, shape1, shape2, i , j):
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
    drawAng(angle, pos2, arrow) """
                    
def add_line(shape1, shape2, i , j):
    # create line between shapes.
    global SHAPE_ID
    global LINE_ID
    try:
        if i != -1 and j != -1:
            shapeId_1 = get_shape_id(shape1)
            shapeId_2 = get_shape_id(shape2)
            edges[shapeId_1].append(LINE_ID)
            edges[shapeId_2].append(LINE_ID)
            directed_graph[shapeId_1].append(shapeId_2)
            lines[LINE_ID] = [(shapes[shapeId_1][2].input_ports[i][0] +shapes[shapeId_1][2].loc[0],
                               shapes[shapeId_1][2].input_ports[i][1] +shapes[shapeId_1][2].loc[1]),
                               (shapes[shapeId_2][2].output_ports[j][0] + shapes[shapeId_2][2].loc[0],
                                shapes[shapeId_2][2].output_ports[j][1] + shapes[shapeId_2][2].loc[1])]
            LINE_ID += 1
    except Exception as e: 
        print(e)
    #except:
        #print("addLine(), problem!")

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
    #find the lines that are connected in hitlist:
    h = []
    for i in range(len(hitlist)):
        if(shape_id == hitlist[i][3]):
            h.append(i)
    return h


def graph_draw(event, screen)-> Tuple[int]:
    global dragging, dragged, dragged_id, dragged_init_pos, selected, offset_x, offset_y, connected_lines
    mousestate = pygame.mouse.get_pressed()
    print(mousestate)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if not dragging:
                for shape_id in shapes:
                    shape = shapes[shape_id][0]
                    m_x, m_y = event.pos
                    checker1 = CheckCircle((m_x, m_y),shapes[shape_id][2].input_ports, shapes[shape_id][2].loc)
                    checker2 = CheckCircle((m_x, m_y),shapes[shape_id][2].output_ports, shapes[shape_id][2].loc)
                    print(checker1, checker2)
                    if checker1 > -1:
                        return ((shapes[shape_id][2].input_ports[checker1][0] + shapes[shape_id][2].loc[0], 
                                shapes[shape_id][2].input_ports[checker1][1] + shapes[shape_id][2].loc[1]), shapes[shape_id], checker1, shape_id, ['in', checker1]) 
                    if checker2 > -1:
                        return ((shapes[shape_id][2].output_ports[checker2][0] + shapes[shape_id][2].loc[0], 
                                shapes[shape_id][2].output_ports[checker2][1] + shapes[shape_id][2].loc[1]),shapes[shape_id], checker2, shape_id, ['out', checker2]) 
                    if(shape.collidepoint(event.pos)):
                        if(selected != shape) and (selected is not None):
                            # draws the line and deselect shape
                            print(selected, shape)
                            add_line(selected, shape, checker1, checker2)
                            selected = None
                            checker1 = checker2 = -1
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
                            print(connected_lines)

                            m_x, m_y = event.pos
                            offset_x = shape.x - m_x
                            offset_y = shape.y - m_y
                            break

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            """"
            if(dragged is not None and dragged_init_pos is not None):
                    if(dragged.x == dragged_init_pos[0] and dragged.y == dragged_init_pos[1]):
                        selected = dragged
                        s = shapes[dragged_id]
                        s[1] = s[2].selected()[1] 
            """
            dragging = False
            dragged = None
            dragged_init_pos = None 

    if event.type == pygame.MOUSEMOTION:
        if dragging:
            #move shape and snap to grid
            m_x, m_y = event.pos
            p_x = round((m_x + offset_x) /
                            grid_square_size)*grid_square_size
            p_y = round((m_y + offset_y) /
                            grid_square_size)*grid_square_size

            #Make sure shape is in bounds
            
                #idx = connected_lines[key]
                #line = lines[key]
                #print(line)
                #line[idx] = (dragged.x , dragged.y)            
            if (p_x < (GAME_FIELD_POS_X + GAME_FIELD_WIDTH) and p_x > (GAME_FIELD_POS_X) and p_y > GAME_FIELD_POS_Y):
                dragged.x = p_x
                dragged.y = p_y
            #move our line properly
            for i in connected_lines:
                h = list(hitlist[i])
                s_id = h[3]
                chk_ls = h[4]
                chkr = chk_ls[1]
                if(chk_ls[0] == "in"):
                    h[0] = (shapes[s_id][2].input_ports[chkr][0] + shapes[s_id][2].loc[0],
                            shapes[s_id][2].input_ports[chkr][1] + shapes[s_id][2].loc[1])
                else:
                    h[0] = (shapes[s_id][2].output_ports[chkr][0] + shapes[s_id][2].loc[0],
                            shapes[s_id][2].output_ports[chkr][1] + shapes[s_id][2].loc[1])

                hitlist[i] = tuple(h)

                #line = lines[key]
                #line[idx] = (dragged.x, dragged.y)
    if mousestate[2] == 1:
        remeber_id = -1
        for shape_id in shapes:
            if(shapes[shape_id][0].collidepoint(event.pos)):
                remember_id = shape_id
        if remember_id != -1:
            shapes.pop(remember_id)    
            
    return (-1,-1)
