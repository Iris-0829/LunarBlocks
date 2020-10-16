import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
grid_square_size = 15 #10x10px  
FPS = 30
pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()


clock = pygame.time.Clock()

operators = {}
operands = {}
sprites = pygame.sprite.Group()


class TempShape(pygame.sprite.Sprite):

    def __init__(self, color, width, height, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.rect(self.image, color, [0,0, width, height])
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, self.pos)



rectSet = []
lineSet = []

for i in range(10):
    rectSet.append(pygame.Rect(20*i, 20*i, 30, 30))

button = pygame.Rect(300, 400, 150, 75)


def game_loop():
    dragging = False
    dragged = None
    dragged_init_pos = None
    selected = None


    points = None

    drawing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if(button.collidepoint(event.pos)):
                        rectSet.append(pygame.Rect(200, 200, 30, 30))
                    else:
                        for rectangle in rectSet:
                            if(rectangle.collidepoint(event.pos)):
                                if(selected != rectangle) and (selected is not None):
                                    #draw line
                                    lineSet.append([(selected.x, selected.y), (rectangle.x, rectangle.y)])
                                    selected = None
                                    break
                                else:
                                    dragging = True
                                    dragged = rectangle
                                    dragged_init_pos = (rectangle.x, rectangle.y)
                                    m_x, m_y = event.pos
                                    offset_x = rectangle.x - m_x
                                    offset_y = rectangle.y - m_y
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


            screen.fill((255,255,255))
            pygame.draw.rect(screen, (0, 255, 0), button)
            for rectangle in rectSet:
                pygame.draw.rect(screen, (0, 0, 0), rectangle)
            for line in lineSet:
                pygame.draw.line(screen, (255,0,0), line[0], line[1], 2)
            
            pygame.display.flip()





game_loop()
pygame.quit()
