import pygame
from pygame import *
from constants import *

class Sand:
    def __init__(self, is_alive, color, x, y):
        self.__x = x * SAND_SCALE
        self.__y = y * SAND_SCALE
        self.__rect = pygame.Rect(self.__x, self.__y, SAND_SCALE, SAND_SCALE)
        self.__is_alive = is_alive
        self.__color = color 
       
           
    def draw(self, window):
        pygame.draw.rect(window, self.__color , self.__rect)
        
    def set_alive(self, is_alive):
        self.__is_alive = is_alive    
        
    def get_alive(self):
        return self.__is_alive     
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        