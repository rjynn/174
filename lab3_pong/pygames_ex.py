import pygame
from pygame.locals import *
from uagame import Window


def print_corners(rect):
    #this function takes a pygame.Rect object and prints
    #each of the rect object's corner's x,y position
    print("Current Corners")
    print(rect.topleft, flush=True)
    print(rect.bottomleft, flush=True)
    print(rect.topright, flush=True)
    print(rect.bottomright, flush=True)

def keydown(rect):
    list_of_keys_pressed = pygame.key.get_pressed() #get list of buttons pressed
    #can also use pygame.key.set_repeat(delay, interval) before this to allow holding keys
    if list_of_keys_pressed[K_a]:
        #rect object down
        print("t pressed")
    else:
        print("something else pressed")
    

def main():
    rect = pygame.Rect(0,0,10,100) #create new rect object 
    print_corners(rect) #print out corners from user-defined function
    rect.move(10,10) #move rect using built-in rect method
    print_corners(rect)
    window = Window("test", 400, 500) #create window

    #===== new code for pong v3 ======#
    while True:
        event = pygame.event.poll() #get event from queue
        if event.type == KEYDOWN: #if event is someone pushing a key
            keydown(rect) #calling function giving rect
    
    
    

main()
    