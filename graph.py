import pygame
from data_manager import * 

def add_line(shape1, shape2):
    # create line between shapes.
    global SHAPE_ID
    global LINE_ID
    try:
        shapeId_1 = get_shape_id(shape1)
        shapeId_2 = get_shape_id(shape2)
        edges[shapeId_1].append(LINE_ID)
        edges[shapeId_2].append(LINE_ID)
        directed_graph[shapeId_1].append(shapeId_2)
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

def graph_draw(event):
    global dragging, dragged, dragged_id, dragged_init_pos, selected, offset_x, offset_y, connected_lines
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
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
            m_x, m_y = event.pos
            p_x = round((m_x + offset_x) /
                            grid_square_size)*grid_square_size
            p_y = round((m_y + offset_y) /
                            grid_square_size)*grid_square_size

            #Make sure shape is in bounds
            if (p_x < (GAME_FIELD_POS_X + GAME_FIELD_WIDTH) and p_x > (GAME_FIELD_POS_X) and p_y > GAME_FIELD_POS_Y):
                dragged.x = p_x
                dragged.y = p_y
            #move our line properly
            for key in connected_lines:
                idx = connected_lines[key]
                line = lines[key]
                line[idx] = (dragged.x, dragged.y)
