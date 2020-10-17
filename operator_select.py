import pygame
import pygame_gui

# We have (according to Jans mock-up) three fields
# I'll call them game_field, operands_field, operator_select_field





def menu_click(event):
    pass

def draw_menu():
    pass

def draw_layout(ui_man, SCREEN_HEIGHT, SCREEN_WIDTH):
    game_panel_rect = pygame.Rect(
        SCREEN_WIDTH//5, SCREEN_HEIGHT//3, (4*SCREEN_WIDTH)//5, 2*SCREEN_HEIGHT//3)
    input_panel_rect = pygame.Rect(SCREEN_WIDTH//5, 0, 2*SCREEN_WIDTH//5, (SCREEN_HEIGHT//3))

    output_panel_rect = pygame.Rect(3*SCREEN_WIDTH//5, 0, 2*SCREEN_WIDTH//5, (SCREEN_HEIGHT//3))
    operators_panel_rect = pygame.Rect(0, 0, SCREEN_WIDTH//5, SCREEN_HEIGHT) 

    game_panel = pygame_gui.elements.UIPanel(
        relative_rect=game_panel_rect,
        starting_layer_height=0,
        manager=ui_man
    )
    input_panel = pygame_gui.elements.UIPanel(
        relative_rect=input_panel_rect,
        starting_layer_height=0,
        manager=ui_man
    )
    output_panel = pygame_gui.elements.UIPanel(
        relative_rect=output_panel_rect,
        starting_layer_height=0,
        manager=ui_man
    )
    operators_panel = pygame_gui.elements.UIPanel(
        relative_rect=operators_panel_rect,
        starting_layer_height=0,
        manager=ui_man
    )
