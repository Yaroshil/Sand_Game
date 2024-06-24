import random as rd
from constants import *
import pygame
from pygame import *
import sand_class as sand_c

timer = pygame.time.Clock()
last_ticks = pygame.time.get_ticks()
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

sup_color = None
def rand_color():
    value = 0.30 + rd.randint(0,70) / 100
    r = SAND_COLOR[0] * value
    g = SAND_COLOR[1] * value
    b = SAND_COLOR[2] * value
    
    return(r,g,b)

game_active = True

land = [[sand_c.Sand(rd.randint(0, 3) == 0,rand_color(), j, i)  for j in range(HEIGHT_COUNT)] for i in range(WIDTH_COUNT)]# False


while game_active:
    #1 Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            game_active = False
            break 
        
    #2 Логика игры
    new_land = [[sand_c.Sand(False,land[i][j].get_color(), j, i) for j in range(HEIGHT_COUNT)] for i in range(WIDTH_COUNT)]
    
    for i in range(WIDTH_COUNT):
            for j in range(HEIGHT_COUNT):                              
                if not land[i][j].get_alive():
                    continue        
                
                new_i = i + 1 
                new_j = j + 0 
                
            
                if new_i >= WIDTH_COUNT:
                    new_land[WIDTH_COUNT - 1][j].set_alive(True)
                    continue
                
                if new_j >= HEIGHT_COUNT:
                    continue
                
                
            
                if not land[new_i][new_j].get_alive(): 
                    new_land[new_i][new_j].set_alive(True)
                    new_land[new_i][new_j].set_color(land[i][j].get_color())
                
                else:
                    
                    col1 = land[i][j].get_color()
                    col2 = land[new_i][new_j].get_color() 
                                  
                    col_condition_under = col1[0] < col2[0] or col1[1] < col2[1] or col1[2] < col2[2]
                   
                    
                    
                    dir = rd.choice([-1,1])   
                                                                                                
                    if j == 0:
                        sup_color = land[i +1][j + 1].get_color()
                         
                        col_condition_L = sup_color[0] > col1[0] or\
                                          sup_color[1] > col1[1] or\
                                          sup_color[2] > col1[2]
                                          
                                          
                        #если песчинка на левом краю
                        if not land[i + 1][j + 1].get_alive():
                            if rd.randint(1,10) in (1,2,3):
                                new_land[i][j + 1].set_alive(True)
                                land[i][j].set_alive(False)#
                            
                        elif col_condition_L:
                                new_land[i +1][j + 1].set_color(col1)
                                new_land[i][j].set_color(sup_color)                                                                       
                             
                    elif  j == HEIGHT_COUNT - 1:
                        sup_color = land[i +1][j - 1].get_color()
                        
                        col_condition_R = sup_color[0] > col1[0] or\
                                          sup_color[1] > col1[1] or\
                                          sup_color[2] > col1[2]
                                          
                         #если песчинка на правом краю 
                        if not land[i + 1][j - 1].get_alive():
                            if rd.randint(1,10) in (1,2,3):
                                new_land[i +1][j - 1].set_alive(True)
                                land[i][j].set_alive(False)#
                            
                        elif col_condition_R:
                            new_land[i +1][j - 1].set_color(col1)
                            new_land[i][j].set_color(sup_color) 
                                
                                
                    else:  
                        sup_color = land[i + 1][j + dir ].get_color()
                        
                        col_condition_helper =  sup_color[0] > col1[0] or\
                                                sup_color[1] > col1[1] or\
                                                sup_color[2] > col1[2] 
                                               
                                                                                
                                                                                                                         
                        if not land[i + 1][j + dir].get_alive():
                            if rd.randint(1,10) <= 3:                               
                                new_land[i +1][j + dir].set_alive(True)
                                land[i][j].set_alive(False)#
                                
                        elif col_condition_helper:
                                new_land[i +1 ][j + dir ].set_color(col1)
                                new_land[i][j].set_color(sup_color)
                                                                  
                                                                                                                                                                         
                        elif not land[i + 1][j - dir].get_alive() : 
                            if rd.randint(1,10) in (1,2,3):               
                                new_land[i +1][j - dir ].set_alive(True)
                                land[i][j].set_alive(False)#
                                
                        elif col_condition_helper:
                                    sup_color = land[i +1][j - dir ].get_color()
                                    new_land[i + 1][j - dir ].set_color(col1)
                                    new_land[i][j].set_color(sup_color)
                    
                    
                                                                                                               
                    if col_condition_under:
                        new_land[i][j].set_color(col2)
                        new_land[new_i][new_j].set_color(col1)
                        
                        
                    new_land[i][j].set_alive(land[i][j].get_alive()) 
                                                                                           
                                                                        
    land = new_land
    
    buttons = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()    
    
    if buttons[0] and (pygame.time.get_ticks() - last_ticks >= TICKS_DIFFERENT):
        matrix_pos = (pos[0] // SAND_SCALE, pos[1] // SAND_SCALE)
        #print(matrix_pos)
        
        if (SAND_GROUP_SIZE <= matrix_pos[0] < HEIGHT_COUNT - SAND_GROUP_SIZE) and (SAND_GROUP_SIZE <= matrix_pos[1] < WIDTH_COUNT - SAND_GROUP_SIZE):
           land[matrix_pos[1]][matrix_pos[0]].set_alive(True)
           land[matrix_pos[1]][matrix_pos[0]].set_color(rand_color()) 
           
        
           for offset in OFFSETS:                            
                if rd.randint(0,3) in (1,2,3): 
                    new_pos = (matrix_pos[0] + offset[0], matrix_pos[1] + offset[1])
                    
                    land[new_pos[1]][new_pos[0]].set_alive(True)
                    land[new_pos[1]][new_pos[0]].set_color(rand_color())
            
               
           
           
        last_ticks = pygame.time.get_ticks()   
            
            
            
    #3 Отображение
    window.fill(BLACK)
    
    for i in range(WIDTH_COUNT):
        for j in range(HEIGHT_COUNT):
            if land[i][j].get_alive():                 
                land[i][j].draw(window)
                
    pygame.display.update()
    timer.tick(FPS)
    
pygame.quit()

'''
import random as rd
from constants import *
import pygame
from pygame import *
import sand_class as sand_c

timer = pygame.time.Clock()
last_ticks = pygame.time.get_ticks()
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

sup_color = None
def rand_color():
    value = 0.3 + rd.randint(0,70) / 100
    r = SAND_COLOR[0] * value
    g = SAND_COLOR[1] * value
    b = SAND_COLOR[2] * value
    
    return(r,g,b)

game_active = True

land = [[sand_c.Sand(rd.randint(0, 9) == 0,rand_color(), j, i)  for j in range(HEIGHT_COUNT)] for i in range(WIDTH_COUNT)]# False


while game_active:
    #1 Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            game_active = False
            break 
        
    #2 Логика игры
    new_land = [[sand_c.Sand(False,land[i][j].get_color(), j, i) for j in range(HEIGHT_COUNT)] for i in range(WIDTH_COUNT)]
    
    for i in range(WIDTH_COUNT):
            for j in range(HEIGHT_COUNT):                              
                if not land[i][j].get_alive():
                    continue        
                
                new_i = i + 1 
                new_j = j + 0 
                
            
                if new_i >= WIDTH_COUNT:
                    new_land[WIDTH_COUNT - 1][j].set_alive(True)
                    continue
                
                if new_j >= HEIGHT_COUNT:
                    continue
                
                
            
                if not land[new_i][new_j].get_alive(): 
                    new_land[new_i][new_j].set_alive(True)
                    new_land[new_i][new_j].set_color(land[i][j].get_color())
                
                else:
                    
                    col1 = land[i][j].get_color()
                    col2 = land[new_i][new_j].get_color() 
                                  
                    col_condition_under = col1[0] < col2[0] or col1[1] < col2[1] or col1[2] < col2[2]
                   
                    
                    
                    dir = rd.choice([-1,1])   
                                                                                                
                    if j == 0:                                                                    
                        #если песчинка на левом краю
                        if not land[i + 1][j + 1].get_alive():
                            new_land[i + 1][j + 1 ].set_alive(True)
                            land[i][j].set_alive(False) #new_land[i][j].set_alive(False)
                                                                                                 
                             
                    elif  j == HEIGHT_COUNT - 1:
                        #если песчинка на правом краю 
                        if not land[i + 1][j - 1].get_alive():
                            new_land[i + 1][j - 1].set_alive(True)
                            land[i][j].set_alive(False) #new_land[i][j].set_alive(False)
                                                                                  
                    else:                                                                                                                                                                                                                                                                          
                        if not land[i + 1][j + dir].get_alive():                               
                                new_land[i + 1][j + dir ].set_alive(True)
                                land[i][j].set_alive(False) #new_land[i][j].set_alive(False)
                                                                                                                                                                                                       
                        elif not land[i + 1][j - dir].get_alive():                
                                new_land[i + 1][j - dir ].set_alive(True)
                                land[i][j].set_alive(False) #new_land[i][j].set_alive(False)
                                                    
                                                                                                                                                                                                                      
                    if col_condition_under:
                        new_land[i][j].set_color(col2)
                        new_land[new_i][new_j].set_color(col1)
                        
                        
                    new_land[i][j].set_alive(land[i][j].get_alive()) 
                                                                                           
                                                                        
    land = new_land
    
    buttons = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()    
    
    if buttons[0] and (pygame.time.get_ticks() - last_ticks >= TICKS_DIFFERENT):
        matrix_pos = (pos[0] // SAND_SCALE, pos[1] // SAND_SCALE)
        
        if (0 <= matrix_pos[0] < HEIGHT_COUNT) and (0 <= matrix_pos[1] < WIDTH_COUNT):
           land[matrix_pos[1]][matrix_pos[0]].set_alive(True)
           land[matrix_pos[1]][matrix_pos[0]].set_color(rand_color()) 
           
        
           for offset in OFFSETS:
               new_pos = (matrix_pos[0]+offset[0],) + (matrix_pos[1]+offset[1],)
               land[new_pos[1]][new_pos[0]].set_alive(True)
               land[new_pos[1]][new_pos[0]].set_color(rand_color())
                                          
        last_ticks = pygame.time.get_ticks()   
            
            
            
    #3 Отображение
    window.fill(BLACK)
    
    for i in range(WIDTH_COUNT):
        for j in range(HEIGHT_COUNT):
            if land[i][j].get_alive():                 
                land[i][j].draw(window)
                
    pygame.display.update()
    timer.tick(FPS)
    
pygame.quit()
'''        
              