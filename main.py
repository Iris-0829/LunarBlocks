import pygame
from collections import defaultdict
from components.Addition import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
grid_square_size = 15 #15x15px  
FPS = 30
lineId = 0
shapeId = 0
pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()


clock = pygame.time.Clock()

operatorSet = []
operandSet = []
shapes = {}
edges = {}
edgeSet = defaultdict(list)
sites = pygame.sprite.Group()


def addLine(shape1, shape2):
    #create line between shapes.
    global shapeId
    global lineId
    try:
        shapeId_1 = getShapeId(shape1)
        shapeId_2 = getShapeId(shape2)
        edgeSet[shapeId_1].append(lineId)
        edgeSet[shapeId_2].append(lineId)
        edges[lineId] = [(shape1.x, shape1.y), (shape2.x, shape2.y)]
        lineId += 1
    except:
        print("addLine(), problem!")   
    return

def addShape(shape):
    global shapeId
    shapes[shapeId] = shape
    shapeId += 1

def getShapeId(shape):
    global shapeId
    for id in shapes:
        if(shapes[id] == shape):
            return id
    shapes[shapeId] = shape
    shapeId += 1
    return shapeId - 1

for i in range(10):
    addShape(pygame.Rect(10*i, 5*i, 30, 30))



def game_loop():
    dragging = False
    dragged = None
    dragged_init_pos = None
    dragged_id = -1

    selected = None
    drawing = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #if(button.collidepoint(event.pos)):
                    #    operatorSet.append(pygame.Rect(200, 200, 30, 30))
                    #else:
                        for sId in shapes:
                            shape = shapes[sId] 
                            if(shape.collidepoint(event.pos)):
                                if(selected != shape) and (selected is not None):
                                    #draw line
                                    addLine(selected, shape)
                                    selected = None
                                    break
                                else:
                                    dragging = True
                                    dragged = shape
                                    dragged_id = getShapeId(dragged)
                                    dragged_init_pos = (shape.x, shape.y)
                                    m_x, m_y = event.pos
                                    offset_x = shape.x - m_x
                                    offset_y = shape.y - m_y
                                    break
                                
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if(dragged is not None and dragged_init_pos is not None):
                        if(dragged.x == dragged_init_pos[0] and dragged.y == dragged_init_pos[1]):
                            selected = dragged
                    dragging = 0
                    dragged = None


            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    m_x, m_y = event.pos
                    dragged.x = round((m_x + offset_x) / grid_square_size)*grid_square_size
                    dragged.y = round((m_y + offset_y) / grid_square_size)*grid_square_size
                    if dragged_id in edgeSet.keys():
                        for id in edgeSet[dragged_id]:
                            line = edges[id]
                            if line[0] == dragged_init_pos:
                                line[0] = (dragged.x, dragged.y)
                            else:
                                line[1] = (dragged.x, dragged.y)
                            edges[id] = line


            screen.fill((255,255,255))
            #pygame.draw.rect(screen, (0, 255, 0), button)
            for shape in shapes:
                pygame.draw.rect(screen, (0, 0, 0), shapes[shape])
            
            for line in edges:
                pygame.draw.line(screen, (0, 0, 255),
                                 edges[line][0], edges[line][1], 2)
            

            pygame.display.flip()





game_loop()
pygame.quit()
