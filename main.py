from pygame import gfxdraw
import pygame_gui
import time
from operator_select import draw_layout
from components.needs_node_version.Subtraction import *
from components.commands.AdditionNode import *
#from operator_select import *
from components.CreateOperator import CreateOperator
from scenes.Level import *
from graph import *
from components.ScrollBar import ScrollBar
from scenes.Level import *




pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()
ui_man = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "theme.json")


# ==========operator_select_field===========================

up_button_img = pygame.image.load("assets/up_button.png")
down_button_img = pygame.image.load("assets/down_button.png")
play_button_img = pygame.image.load("assets/play_button.png")
up_button_rect = up_button_img.get_rect(center=(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT // 20))
down_button_rect = down_button_img.get_rect(center=(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.8))
play_button_rect = play_button_img.get_rect(center=(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4))

def draw_button(screen):
    screen.blit(up_button_img, up_button_rect)
    screen.blit(down_button_img, down_button_rect)
    screen.blit(play_button_img, play_button_rect)

#Spawn in middle of game field:
operators = []
square_operator = CreateOperator(screen, "assets/triangle_add.png",
                                 (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 5),
                                    ((GAME_FIELD_WIDTH + GAME_FIELD_POS_X)//2,
                                     (GAME_FIELD_HEIGHT + GAME_FIELD_POS_Y)//2), "AdditionNode")
operators.append(square_operator)
ineq_operator = CreateOperator(screen, "assets/ineq.png",
                                 (SCREEN_WIDTH // 16, 2 * SCREEN_HEIGHT // 5),
                                    ((GAME_FIELD_WIDTH + GAME_FIELD_POS_X)//2,
                                     (GAME_FIELD_HEIGHT + GAME_FIELD_POS_Y)//2), "IneqNode")
operators.append(ineq_operator)
eq_operator = CreateOperator(screen, "assets/eq.png",
                                 (SCREEN_WIDTH // 16, 3 * SCREEN_HEIGHT // 5),
                                    ((GAME_FIELD_WIDTH + GAME_FIELD_POS_X)//2,
                                     (GAME_FIELD_HEIGHT + GAME_FIELD_POS_Y)//2), "eqNode")
operators.append(eq_operator)

scroll = ScrollBar(screen, "assets/scrollbar.png", (SCREEN_WIDTH // 6, SCREEN_WIDTH // 9), operators)

# ========================================

clock = pygame.time.Clock()

# TODO: clean this up
# It doesn't really need to be in this file.
# I'll keep it around for now though. 


# Modified from https://stackoverflow.com/questions/56295712/how-to-draw-a-dynamic-arrow-in-pygame
def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pts = ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad)))
    pygame.gfxdraw.aapolygon(screen, pts, tricolor)
    pygame.gfxdraw.filled_polygon(screen, pts, tricolor)


# ==============================================================
# For Testing Purposes
# ================================================================

draw_layout(ui_man, SCREEN_HEIGHT, SCREEN_WIDTH)
#ui_man.set_visual_debug_mode(True)
#============================================================================

def game_loop():
    START_FADE = False
    level = GameScene(1, screen)
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    scroll.is_holding(event.pos)
                    square_operator.isOn(event.pos)
                    ineq_operator.isOn(event.pos)
                    eq_operator.isOn(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                scroll.release()
                if up_button_rect.collidepoint(event.pos):
                    square_operator.change_loc(SCREEN_HEIGHT // 50)
                    ineq_operator.change_loc(SCREEN_HEIGHT // 50)
                    eq_operator.change_loc(SCREEN_HEIGHT // 50)
                elif down_button_rect.collidepoint(event.pos):
                    square_operator.change_loc(-SCREEN_HEIGHT // 50)
                    ineq_operator.change_loc(-SCREEN_HEIGHT // 50)
                    eq_operator.change_loc(-SCREEN_HEIGHT // 50)
                    selected = shapes[get_shape_id(level.in_tup[0])][0]

                elif play_button_rect.collidepoint(event.pos):
                    print("play!")
                    START_FADE = True


                # elif play_button_rect.collidepoint(event.pos):
                    # mouse click play_button

            
            if event.type == pygame.MOUSEMOTION:
                scroll.update_loc(event.pos)
           
            #if event == pygame.MOUSEBUTTONDOWN:
            ui_man.process_events(event)

            ui_man.update(time_delta)
            
            screen.fill((255, 255, 255))
            ui_man.draw_ui(screen)
            #PUT ALL GAME ELEMENTS BELOW HERE
            t = level.render(event)
            if t != (-1,-1):
                hitlist.append(t)
            length = len(hitlist)             
            square_operator.display()
            ineq_operator.display()
            eq_operator.display()
            
            scroll.display()
            i = 0
            if(len(hitlist) > 1):
                for item in list(zip(hitlist[::2], hitlist[1::2])):
                    arrow(screen, (255,255,255), (255,255,255), item[0][0], item[1][0], 10, 5)

            for shape_id in shapes:
                screen.blit(shapes[shape_id][1], shapes[shape_id][0])
                shapes[shape_id][2].loc = (shapes[shape_id][0].x, shapes[shape_id][0].y)
                for port_rel_loc in shapes[shape_id][2].input_ports + shapes[shape_id][2].output_ports:
                    shapes[shape_id][2].draw_port(screen, (154, 154, 154), port_rel_loc)                

            #for line in lines:  
            #    arrow(screen, (255,255,255), (255,255,255), lines[line][0], lines[line][1], 10, 5)

            draw_button(screen)
            if(START_FADE):
                check = pygame.image.load("./assets/checkmark.png").convert()
                i = 0
                while i < 255:
                    i += 255/60
                    check.set_alpha(i)
                    screen.blit(check, check.get_rect())
                while i > 0:
                    i -= 255/30
                    check.set_alpha(i)
                    screen.blit(check, check.get_rect())
                START_FADE = False
            pygame.display.flip()

game_loop()
pygame.quit()
