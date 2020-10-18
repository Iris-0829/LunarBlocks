from collections import defaultdict
from components.commands.InNode import InNode
from components.commands.OutNode import OutNode
import math

#All of this needs to be cleared when a new level starts: 
operator_set = []
operand_set = []
shapes = defaultdict(list)
lines = {}
edges = defaultdict(list)
directed_graph = defaultdict(list)
in_out = []

dragging = False
dragged = None
dragged_init_pos = None
dragged_id = -1
line_num = -1
selected = None
drawing = False
connected_lines = {}
offset_x = 0
offset_y = 0




SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
GAME_FIELD_POS_X = SCREEN_WIDTH//5
GAME_FIELD_POS_Y = SCREEN_HEIGHT//3
GAME_FIELD_WIDTH = 4*SCREEN_WIDTH//5
GAME_FIELD_HEIGHT = 2*SCREEN_HEIGHT//3

grid_square_size = 10  # 10x10px
LINE_ID = 0
SHAPE_ID = 0
FPS = 30
rad = math.pi/180
