
FPS = 60

# Basic
ROW = 5
COL = 5

GEM_SIZE = 70
GRID_SIZE = 75

# Position
BAR_HRIGHT = 10

PUZZLE_X = 0
PUZZLE_Y = BAR_HRIGHT
PUZZLE_WIDTH = GRID_SIZE * ROW
PUZZLE_HEIGHT = GRID_SIZE * COL

ROAD_X = PUZZLE_WIDTH
ROAD_Y = BAR_HRIGHT
ROAD_WIDTH = 750
ROAD_HEIGHT = PUZZLE_HEIGHT

SCREEN_WIDTH = PUZZLE_WIDTH + ROAD_WIDTH
SCREEN_HEIGHT = BAR_HRIGHT + PUZZLE_HEIGHT

# Color
LIGHT_BROWN = (222, 184, 135)   # 浅棕色
DARK_BROWN = (139, 69, 19)      # 深棕色
GRAY = (50, 50, 50)             # 灰色
BLACK = (0, 0, 0)               # 黑色
WHITE = (255, 255, 255)         # 白色
GREEN = (0, 255, 0)             # 綠色
RED = (255, 0, 0)               # 紅色
YELLOW = (255, 255, 0)          # 黃色
ORANGE = (255, 165, 0)          # 橙色

PROGRESS_BASE_COLOR = WHITE
PROGRESS_COLOR = GREEN
HP_BAR_COLOR = RED

# Game
COLOR_LIST = ["blue", "green", "yellow", "red"]

VEHICLE_TYPE = {
    1: "Scooter",
    2: "Car",
    4: "Van",
}
