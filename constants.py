WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_BLACK = (22,26,30)
SAND_COLOR = (253,206,154)


SAND_SCALE = 10

SAND_GROUP_SIZE = 5 // 2


OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1),\
           (-2,-2), (-2,-1), (-2,0), (-2,1), (-1,-2), (-1,2),(1,2), (0,-2),\
            (0,2), (1,-2), (2,-2), (2,-1), (2,0), (2,1), (2,2)]

#3 #OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


HEIGHT_COUNT = WINDOW_HEIGHT // SAND_SCALE
WIDTH_COUNT = WINDOW_WIDTH // SAND_SCALE

TICKS_DIFFERENT = 25
FPS = 140