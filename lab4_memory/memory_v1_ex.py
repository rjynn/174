#written by Ruby/Leo for 174 labs

import pygame
from uagame import Window

#this code shows how to draw image files onto your 
#pygame surface.
#images to be used for this game can be found
#under the "Resources" tab of the lab 4

def main():
    window = Window("Memory", 400, 400) #create window
    image = pygame.image.load("pic.jpg") #get image from file name
    surface = window.get_surface() #get surface to draw image on
    surface.blit(image, (0,0)) #from pygame docs args: image, tuple for coordinates
    window.update() #update the window
    
main()
