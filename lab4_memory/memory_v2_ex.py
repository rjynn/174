import pygame
from uagame import Window
from pygame.locals import *


def main():
    window = Window("Memory v2", 400, 400)
    while True:
        event = pygame.event.poll() #grab event from q
        if event.type == MOUSEBUTTONUP: #if it was a mouse click
            print(event.pos) #checks position that event occurred
            
    
    
main()
